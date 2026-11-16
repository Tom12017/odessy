import asyncio
from dataclasses import replace

import httpx

from odessy.application.api import create_app
from odessy.application.desktop_voice import DesktopVoice
from odessy.application.voice_configuration import LiveVoiceConfiguration
from odessy.setup.contracts import SetupSelection
from odessy.application.capabilities import configuration_descriptor


def test_saved_voice_applies_without_changing_model_or_workspace_and_defers_busy():
    async def run():
        original = SetupSelection.from_dict({'role': 'combined', 'model': {'provider': 'ollama', 'name': 'old'}})
        saved = replace(original, voice=replace(original.voice, enabled=True, audio_input_device='new-device'))
        state = {'selection': saved}
        voice = DesktopVoice(lambda: None, host='fixture')
        live = LiveVoiceConfiguration(voice, original, '/original', 'owner', lambda: state['selection'])
        descriptor = configuration_descriptor(original, '/original', owner='owner')
        app = create_app(lambda: None, token='test', desktop_voice=voice,
                         runtime_configuration=descriptor, voice_configuration=live)
        path = '/v1/voice/configuration'
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://test') as client:
            assert (await client.post(path, json={})).status_code == 401
            client.headers['Authorization'] = 'Bearer test'
            fingerprint = configuration_descriptor(saved, '/original', owner='owner')['fingerprint']
            assert (await client.post(path, json={'fingerprint': 'stale'})).status_code == 409
            voice.owner = 'recording-session'
            result = await client.post(path, json={'fingerprint': fingerprint})
            assert result.json()['status'] == 'deferred'
            assert live.selection.voice == original.voice
            voice.owner = None
            result = await client.post(path, json={'fingerprint': fingerprint})
            assert result.json()['status'] == 'applied'
            assert live.selection.voice.audio_input_device == 'new-device'
            assert app.state.runtime_configuration['fingerprint'] == fingerprint
            assert voice.enabled
            state['selection'] = replace(saved, model=replace(saved.model, name='new-model'))
            await live.refresh(app)
            assert live.selection.model.name == 'old'
            assert app.state.runtime_configuration['model']['name'] == 'old'
            state['selection'] = replace(saved, voice=replace(saved.voice, enabled=False))
            await live.refresh(app)
            assert not voice.enabled
            assert voice.snapshot(type('Controller', (), {'id': 's'})())['supported'] is False
    asyncio.run(run())


def test_invalid_saved_configuration_keeps_active_audio():
    async def run():
        selection = SetupSelection(role='combined')
        voice = DesktopVoice(lambda: None, host='fixture')
        def invalid():
            raise ValueError('damaged settings')
        live = LiveVoiceConfiguration(voice, selection, '/workspace', 'owner', invalid)
        app = type('App', (), {'state': type('State', (), {})()})()
        try:
            await live.refresh(app)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid configuration must not be acknowledged')
        assert live.selection == selection
    asyncio.run(run())


def test_voice_selection_clears_old_device_and_uses_default_wake_asset(monkeypatch):
    from odessy.voice.config import VoiceConfig
    monkeypatch.setenv('ODESSY_AUDIO_INPUT_DEVICE', 'stale-device')
    config = VoiceConfig.from_selection(SetupSelection(role='combined').voice)
    assert config.audio_input_device == ''
    assert str(config.wake_model).endswith('hey_jarvis_v0.1.onnx')


def test_installed_loader_reads_new_saved_selection(tmp_path, monkeypatch):
    import json
    from test_setup_installed import make_installation
    from odessy.setup import installed
    root = tmp_path / 'app'
    make_installation(root, model=True)
    captured = {}
    monkeypatch.setenv('ODESSY_API_TOKEN', 'fixture')
    monkeypatch.setattr('odessy.setup.service_entry.run', lambda *a, **kw: captured.update(kw))
    installed.serve(['--root', str(root), '--port', '18765'])
    selection = SetupSelection.from_dict({'role': 'combined', 'model': {'provider': 'ollama', 'name': 'same'},
                                         'voice': {'enabled': True, 'audio_input_device': 'fresh'}})
    from odessy.setup.contracts import public
    (root / 'configuration.json').write_text(json.dumps({'schema_version': 1, 'selection': public(selection), 'workspace': str(tmp_path / 'work')}))
    assert captured['voice_selection_loader']().voice.audio_input_device == 'fresh'


def test_deferred_reload_is_applied_automatically_after_owner_releases():
    async def run():
        selection = SetupSelection(role='combined')
        saved = replace(selection, voice=replace(selection.voice, enabled=True))
        voice = DesktopVoice(lambda: None, host='fixture')
        live = LiveVoiceConfiguration(voice, selection, '/work', 'owner', lambda: saved)
        app = create_app(lambda: None, token='fixture', desktop_voice=voice,
                         runtime_configuration=configuration_descriptor(selection, '/work', owner='owner'),
                         voice_configuration=live)
        voice.owner = 'busy'
        async with app.router.lifespan_context(app):
            await asyncio.sleep(0.6)
            assert live.selection == selection
            voice.owner = None
            await asyncio.sleep(0.6)
            assert live.selection.voice.enabled
        assert voice.owner is None
    asyncio.run(run())
