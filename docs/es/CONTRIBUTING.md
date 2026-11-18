# Contribuir a Odessy

[English](../../CONTRIBUTING.md) | [简体中文](../zh-CN/CONTRIBUTING.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha**

Empezar por la [configuración gestionada del escritorio](./getting-started.md), los [issues abiertos de GitHub](https://github.com/Trisoma/odessy/issues), la [matriz de soporte](current-status.md) y la [arquitectura](ARCHITECTURE.md). Buscamos colaboradores capaces de llevar un área concreta a través de la revisión; la disponibilidad voluntaria es bienvenida.

> Una breve historia de este proyecto en [Story](../../Story.md) (solo en inglés).

¡Bienvenidos a bordo! ⛵ Gracias por ayudar a mejorar Odessy. Los informes de errores, las correcciones concretas y una documentación más clara ayudan a que esta Developer Preview sea más fácil de usar. Esta guía explica por dónde empezar, cómo preparar el entorno y qué incluir al enviar un cambio.

Para una visión general del proyecto, empezar por el [README](../../README.es.md). La arquitectura y la documentación de componentes comienzan en el [índice de documentación](./README.md).

## Elegir por dónde empezar

| Contribución | Cómo empezar |
|---|---|
| Correcciones de errores y de documentación pequeñas | Abrir un pull request concreto directamente. Vincular un issue existente cuando corresponda. |
| Nuevas funcionalidades, mejoras o cambios más grandes | Abrir primero un issue para explicar el problema y el enfoque propuesto antes de empezar la implementación. |
| Cambios solo de refactorización o de CI | No abrir pull requests independientes para estos cambios. |
| Vulnerabilidades de seguridad | Seguir [SECURITY.md](../../SECURITY.md) (solo en inglés). No revelar vulnerabilidades en issues públicos. |

Es bienvenido reportar un problema aunque no se pueda implementar una corrección. Indicar si se planea trabajar en él para que otras personas puedan coordinarse.

## Ruta hacia la responsabilidad de un área

1. Elegir un [issue abierto de GitHub](https://github.com/Trisoma/odessy/issues), reproducir el comportamiento y comentar con el alcance propuesto. Revisar la discusión y las asignaciones actuales antes de empezar, y buscar trabajo que se solape.
2. Enviar un único PR concreto con sus comprobaciones de aceptación. Explicar qué evidencia proviene de fixtures y qué evidencia proviene de proveedores o hardware reales. La primera contribución puede ser una prueba de regresión, una mejora de diagnóstico, una corrección de presentación o un informe de benchmark reproducible.
3. Tras contribuciones revisadas, proponer la responsabilidad de un área concreta: mantener sus pruebas y documentación, clasificar los informes pertinentes y ayudar a revisar cambios posteriores. Acordar los límites y la disponibilidad con el mantenedor del proyecto en un issue público.
4. Los permisos del repositorio o un rol de mantenedor concreto requieren una decisión explícita por separado. Un PR fusionado, la autoasignación o un plan escrito por IA no otorgan acceso.

La política y el despacho, las credenciales, el emparejamiento y la identidad del host, la propiedad de la instalación y la seguridad de la restauración requieren la revisión del propietario del proyecto. El escritorio `lib/app/`, los controladores y los clientes compartidos también requieren la revisión del propietario según su `AGENTS.md`; el trabajo de presentación puede comenzar en los archivos de vista acordados. Leer el [mapa de arquitectura](ARCHITECTURE.md) y las instrucciones locales antes de cambiar un contrato compartido.

Se trata de mantenimiento voluntario, sin un SLA de tiempo de respuesta garantizado. Incluir la reproducción, los criterios de aceptación y las comprobaciones en el issue/PR para que el progreso no dependa de mensajes privados. Si no ha habido respuesta tras una semana, añadir un único recordatorio breve antes de emprender un cambio mayor. La confianza de quien contribuye y los tiempos de respuesta deben demostrarse en interacciones reales; el volumen de commits no prueba ninguna de las dos cosas.

## Antes de abrir un issue

Buscar issues y pull requests existentes, incluidos los cerrados y fusionados, para evitar trabajo duplicado. Revisar el código fuente pertinente y las [limitaciones conocidas](./LIMITATION.md) para conocer el comportamiento y las restricciones existentes. Si ya hay un PR que aborda el problema, considerar ayudar a revisarlo o mejorarlo.

Mantener cada issue centrado en un solo problema. Para un informe de error, incluir:

- La versión o el commit, el sistema operativo, la arquitectura y el backend del modelo.
- Los pasos para reproducir el problema, incluidos los comandos ejecutados.
- El comportamiento esperado y el real, con diagnósticos sin datos sensibles cuando sea útil.

Para una propuesta de funcionalidad, describir el caso de uso, el comportamiento deseado y las alternativas consideradas. Para trabajo más amplio, comentar en el issue antes de empezar para que otras personas contribuyentes puedan evitar esfuerzos superpuestos.

## Preparar un pull request

Apuntar a `develop` y mantener el cambio lo bastante pequeño como para revisarlo. Separar las correcciones no relacionadas, los cambios de formato y las actualizaciones de dependencias.

Antes de solicitar la revisión:

- Explicar el problema y cómo lo resuelve el cambio. Vincular los issues relacionados.
- Añadir o actualizar pruebas para los cambios de comportamiento. Nunca eliminar pruebas ni debilitar las aserciones de seguridad solo para que pasen las comprobaciones. Usar [LIMITATION.md](./LIMITATION.md) para ayudar a determinar si debe corregirse la implementación o una expectativa de prueba.
- Actualizar la documentación cuando cambien la configuración del entorno, la configuración de la aplicación o el comportamiento visible para el usuario.
- Enumerar las comprobaciones exactas ejecutadas y sus resultados, incluidas las fallas, las comprobaciones omitidas y cualquier validación que no se haya podido realizar.
- Eliminar secretos y datos privados del código, los fixtures, los registros y las capturas de pantalla.

## Registro de cambios

Para los cambios visibles para el usuario, añadir una entrada breve en **Unreleased** de [CHANGELOG.md](../../CHANGELOG.md) (solo en inglés). Describir el efecto en los usuarios; omitir la limpieza interna y las ediciones que solo corrigen erratas. Los mantenedores agrupan las entradas bajo una versión y una fecha de publicación al preparar una versión. Mantener la evidencia detallada de calificación y las limitaciones conocidas en las notas de la versión dentro de `docs/releases/`.

## Contribuciones asistidas por IA

Las contribuciones asistidas por IA son bienvenidas; nuestro equipo también usa estas herramientas. Indicar en el PR cuándo se usó asistencia de IA y describir qué se revisó y verificó personalmente. Cada persona sigue siendo responsable de comprender el código enviado, comprobar su comportamiento y confirmar que tiene derecho a contribuirlo.

## Secretos y seguridad

Nunca confirmar claves de API, tokens, grabaciones privadas ni credenciales específicas de una máquina. Ocultar los valores sensibles y la información personal antes de compartir diagnósticos. Si se descubre una vulnerabilidad, usar las instrucciones de reporte privado de [SECURITY.md](../../SECURITY.md) (solo en inglés).

## Configuración del entorno de desarrollo

Los comandos siguientes provienen de [CI](../../.github/workflows/ci.yml) (solo en inglés) y del [CI de la vista previa del escritorio](../../.github/workflows/desktop-preview.yml) (solo en inglés). La CI cubre Python 3.10/3.13 en Ubuntu y 3.12/3.13 en Windows, Node 22/24 en ambas, Rust stable y Flutter 3.47.7 (stable) en Ubuntu. Esta cobertura no establece compatibilidad con hardware, macOS ni proveedores en vivo.

Crear y activar un entorno virtual con Python 3.10-3.13:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Linux, activar con `source .venv/bin/activate`. Usar Node 22 para las comprobaciones de integración de Python y Rust stable para el trabajo de emparejamiento. Desde la raíz del repositorio:

```powershell
cd tools
npm ci --no-audit --no-fund
npm run build
cd ..
python -m pip install -e ".[test,ui]" "pytest-xdist>=3.6,<4"
$env:ODESSY_CONFIG_FILE="$PWD/.ci-no-config.env"
$env:PYTHONUTF8="1"
```

En Linux, usar `export ODESSY_CONFIG_FILE="$PWD/.ci-no-config.env"` y `export PYTHONUTF8=1` en lugar de las asignaciones de entorno de PowerShell.

### Qué espera el inicio rápido

Estos son los requisitos con los que se comprueban los comandos siguientes; la instalación de la aplicación empaquetada no solicita ninguno de ellos.

| Componente | Requisito verificado |
|---|---|
| Python | 3.10–3.13; la CI ejecuta 3.10/3.13 en Ubuntu y 3.12/3.13 en Windows |
| Node | 22 o 24 para el servidor de herramientas (`tools/`), instalado con `npm ci` |
| Flutter | 3.47.7 stable para `apps/desktop`; su SDK de Dart incluido para `packages/odessy_client` |
| Rust | stable, solo para el trabajo de emparejamiento de `native/odessy-link` |

## Ejecutar la aplicación de escritorio

Usar [Primeros pasos](./getting-started.md) para el arranque gestionado por el escritorio ya configurado. La aplicación inicia el servicio y gestiona la autenticación local. Configurar un modelo real en Settings → Models and connections (Configuración → Modelos y conexiones) para la [ruta dorada](./GOLDEN_PATH.md). Las pruebas de arranque desde el código fuente incluyen `local_desktop_application_test.dart`, `source_setup_wiring_test.dart` y la prueba opcional `source_model_integration_test.dart` en `apps/desktop/test/`. La última usa un servicio Python real y un fixture de proveedor en loopback, no inferencia de pago.

## Comprobaciones avanzadas de componentes y API

La CLI del módulo sigue implementada para diagnósticos, uso sin interfaz y pruebas de integración. Estos comandos de servidor manual no son necesarios para usar el escritorio gestionado. Todo lo siguiente no necesita un proveedor de pago, un micrófono ni un host remoto. Un modelo falso determinista comprueba la conexión interna de los componentes; no valida un modelo real, la experiencia de aprobación en vivo, el habla ni la ejecución remota.

Iniciar el backend (esto imprime la dirección de loopback; la API necesita un token):

```powershell
$env:ODESSY_API_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
python -m odessy serve --fake-model
```

Iniciar la aplicación de escritorio en una segunda terminal:

```powershell
cd apps/desktop
flutter run -d windows
```

En Linux, generar un token local e iniciar el servidor con:

```sh
export ODESSY_API_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
python -m odessy serve --fake-model
```

Después, ejecutar `flutter run -d linux` desde `apps/desktop`. Usar el token generado al conectar la aplicación de escritorio. Mostrarlo localmente con `$env:ODESSY_API_TOKEN` en PowerShell o `printf '%s\n' "$ODESSY_API_TOKEN"` en Linux antes de introducirlo en la aplicación. Mantenerlo privado. Generar un token distinto en cada máquina.

Hacer clic en el icono de conexión, introducir la dirección de loopback impresa y el token, y luego enviar `what time is it?`. El token permanece en la memoria de la aplicación; el backend nunca lo imprime. Sin `--fake-model`, los mismos pasos usan el modelo real configurado y su presupuesto existente, y eso es lo que hace que las comprobaciones con proveedores en vivo sean trabajo aparte. Borrar primero la anulación del inicio rápido (`unset ODESSY_CONFIG_FILE` en Linux o `Remove-Item Env:ODESSY_CONFIG_FILE` en PowerShell), o apuntarla a la configuración personal. De lo contrario, la ejecución en vivo seguirá usando `.ci-no-config.env`.

`python -m odessy --fake-model "what time is it?"` ejecuta el mismo bucle de texto sin el escritorio, que es la comprobación de extremo a extremo más pequeña del lado de Python.

## Diagnosticar este equipo

```sh
python -m odessy doctor
python -m odessy doctor --voice
```

`doctor` nombra cada paso fallido u opcional junto con una solución, por ejemplo un endpoint de modelo que no responde, un directorio `tools/` sin compilar o los recursos opcionales de habla y de palabra de activación. Las comprobaciones de Piper y de proveedores personalizados están incompletas; usar también sus pruebas controladas de proveedores. Un `[FAIL]` para el endpoint del modelo es esperable antes de que se ejecute Ollama (u otro endpoint) y no bloquea las comprobaciones de modelo falso anteriores. No descarga recursos ni realiza inferencia en la nube, pero puede sondear endpoints configurados y listar herramientas de terceros. No es una réplica completa de las credenciales de sesión del escritorio ni una prueba de aceptación de audio físico. Mantener el error visible del escritorio y la configuración seleccionada junto a su salida.

## Ejecutar las comprobaciones pertinentes

Ejecutar las comprobaciones de los componentes modificados e incluir los comandos y resultados exactos en el PR. Indicar qué comprobaciones no se pudieron ejecutar y por qué.

### Entorno de ejecución de Python

Desde la raíz del repositorio:

```sh
python -m pytest -q -n 2 --dist loadfile --tb=short --durations=10
python -m odessy --help
python -m odessy --fake-model "what time is it?"
python -m odessy --fake-model "list ."
```

La CI comprueba que las respuestas del modelo falso comiencen con `The current time is ` y `Directory entries: ` respectivamente, y que la respuesta del directorio incluya `pyproject.toml`. Son comprobaciones de conexión interna, no una aceptación de modelo real.

### Servidor de herramientas Node

Desde `tools/`:

```sh
npm ci --no-audit --no-fund
npm run typecheck
npm test
```

### Transporte y emparejamiento en Rust

Desde `native/odessy-link/`:

```sh
cargo test --locked
cargo clippy --all-targets -- -D warnings
cargo build --locked
```

Para la integración emparejada, compilar primero Node y Rust, establecer `ODESSY_LINK_E2E=1` (PowerShell: `$env:ODESSY_LINK_E2E="1"`) y luego ejecutar en la raíz:

```sh
python -m pytest -q tests/test_paired_transport.py tests/test_paired_integration.py tests/test_paired_agent.py tests/test_paired_host.py
```

### Monitoreo de equipos remotos (SSH)

Usar la [ruta de contribución para SSH](../../src/odessy/ssh/README.md) (solo en inglés) para: un alias existente → probar la conexión → el primer estado con marca temporal → desconectar y reconectar. Incluye los comandos de fixture para un solo portátil, la unión entre proveedor y ciclo de vida, y la solución de problemas. El monitoreo sigue siendo de solo lectura. La selección separada de ejecución SSH de Custom expone `ssh.run` solo después de una acción explícita **Use for agent commands** (Usar para comandos del agente); cada comando remoto exacto requiere aprobación en todos los modos. Se ejecuta como la cuenta SSH sin un sandbox remoto. La ejecución SSH de Harness, la edición remota de archivos y la PTY remota no son compatibles. Consultar [el límite de comandos SSH](../setup/ssh-computers.md) (solo en inglés). Los hosts emparejados ya autenticados siguen siendo un transporte compatible aparte.

### Confinamiento real en Linux

Estas comprobaciones requieren bubblewrap, util-linux y espacios de nombres de usuario sin privilegios utilizables. Consultar la CI para la configuración de AppArmor específica del runner. Establecer `ODESSY_SANDBOX_LIVE=1` y luego ejecutar en la raíz:

```sh
python -m pytest -q tests/test_sandbox_live.py
```

Desde `tools/`, ejecutar `node --test dist/tests/sandbox-live.test.js`. La comprobación de `doctor` en la CI es `python -m odessy doctor | tee doctor.txt; grep -q "read-only: bwrap (full; network cut, credentials hidden)" doctor.txt` bajo Bash en la raíz. Estas comprobaciones necesitan un kernel Linux real; Windows no es suficiente.

### Aplicación de escritorio y cliente Dart

Desde la raíz del repositorio:

```sh
python tool/check_desktop_contracts.py
python -m unittest discover -s tests -p test_desktop_settings_inventory.py -v
```

Desde `packages/odessy_client/`, con el SDK de Dart de Flutter 3.47.7:

```sh
dart pub get
dart format --output=none --set-exit-if-changed lib test
dart analyze
dart test
```

Desde `apps/desktop/`:

```sh
flutter pub get
dart format --output=none --set-exit-if-changed lib test
flutter analyze
flutter test
```

Las comprobaciones de hardware, audio físico, emparejamiento en red real y proveedores en vivo son trabajo de aceptación aparte. Indicar explícitamente cuándo no se ejecutaron.

## Licencia de las contribuciones

Al enviar una contribución, se confirma que se tiene derecho a enviarla y se acepta licenciarla bajo la [licencia Apache-2.0](../../LICENSE) (solo en inglés) del proyecto.
