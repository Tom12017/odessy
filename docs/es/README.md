# Documentación de Odessy

[English](../README.md) | [简体中文](../zh-CN/README.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha**

Empezar por la guía correspondiente a la tarea. La [matriz de soporte actual](current-status.md) define el comportamiento implementado, las capacidades no disponibles y las puertas de publicación pendientes. Los planes históricos y los recibos de pruebas describen las instantáneas registradas, no el soporte actual.

El [candidato Windows del 18 de noviembre](../verification/windows-piper-installer-2026-11-18.md) (solo en inglés) tiene instalación confirmada por el mantenedor, Piper/Kokoro opcional y checksum en el [manual](GOLDEN_PATH.md). Esta página no publica un archivo de versión.

| Tarea | Guía |
| --- | --- |
| Ejecutar la aplicación y verificar una acción local | [Manual de escritorio](./GOLDEN_PATH.md) · [Arranque gestionado desde el código fuente](./getting-started.md) |
| Instalar o gestionar un candidato empaquetado | [Asistente de instalación](../setup/wizard.md) (solo en inglés) · [Instalador](../../installer/README.md) (solo en inglés) |
| Configurar un modelo o credenciales | [Configuración sin interfaz](../setup/headless.md) (solo en inglés) · [Modelos en la nube](../reference/cloud-models.mdx) (solo en inglés) · [Credenciales](../setup/secure-model-credentials.md) (solo en inglés) |
| Usar el escritorio | [Guía del escritorio](../ui/README.md) (solo en inglés) · [Galería de pantallas](../view/README.md) (solo en inglés) |
| Entender los chats guardados y SQLite | [Historial de conversaciones](../ui/conversation-history.md) (solo en inglés) · [Guía de la base de datos](../database/README.md) (solo en inglés) |
| Entender la autoridad de las herramientas | [Modos de acceso](../ui/access-modes.md) (solo en inglés) · [Permisos](../reference/permissions.mdx) (solo en inglés) · [Límites de seguridad](../reference/current-limitations.mdx) (solo en inglés) |
| Usar memoria y documentos | [Contexto, memoria y recuperación](../ui/context-memory-retrieval.md) (solo en inglés) |
| Usar la terminal local o los puntos de control | [Capacidades y límites de seguridad](../ui/terminal-checkpoints.md) (solo en inglés) |
| Conectar equipos | [Configuración de SSH](../setup/ssh-computers.md) (solo en inglés) · [Ejecutor experimental](../setup/executor-preview.md) (solo en inglés) · [Emparejamiento de hosts](../reference/host-pairing.mdx) (solo en inglés) |
| Inspeccionar la telemetría | [Monitoreo](../monitoring/README.md) (solo en inglés) · [API de monitoreo](../monitoring/api.md) (solo en inglés) |
| Trabajar en la voz | [Voz del escritorio](../ui/desktop-voice.md) (solo en inglés) · [Proveedores](../reference/speech-providers.md) (solo en inglés) |
| Contribuir y crecer hacia un área | [Issues abiertos de GitHub](https://github.com/Trisoma/odessy/issues) · [Ruta de contribución y responsabilidad](./CONTRIBUTING.md#ruta-hacia-la-responsabilidad-de-un-área) · [Arquitectura](ARCHITECTURE.md) |
| Preparar una versión | [Alcance de la vista previa alfa](../releases/v0.5.0-alpha.md) (solo en inglés) · [Verificación de la versión](../release-verification.md) (solo en inglés) |

## Interpretar las evidencias correctamente

Las pruebas del código fuente, la CI alojada, las compilaciones nativas, la aceptación instalada, las comprobaciones con proveedores reales y las comprobaciones de hardware responden a preguntas distintas. Una captura de pantalla es evidencia de diseño; no demuestra que una funcionalidad esté disponible en todos los motores o paquetes instalados. Nunca inferir la autoridad de ejecución de herramientas a partir de la conectividad de un dispositivo o de los metadatos del proyecto.
