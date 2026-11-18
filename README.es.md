# Odessy

[English](README.md) | [简体中文](README.zh-CN.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha**

> **Developer Preview inestable.** Odessy es software experimental. Es de esperar encontrar errores, cambios que rompen la compatibilidad y detalles sin pulir. Todavía no existe una versión estable. Consultar [soporte y límites](docs/es/current-status.md) para conocer la cobertura de plataformas y las limitaciones conocidas.

Hola, esto es Odessy, no Odyssey. ⛵

> ¿Curiosidad por cómo empezó? [Leer la historia detrás de Odessy](Story.md) (solo en inglés).

Odessy avanza hacia un **agente personal con la voz como interfaz principal (voice-first)**: un solo escritorio coordina modelos locales o en la nube y el trabajo revisado en el portátil o en un equipo Linux conectado. La inspiración a largo plazo es JARVIS/FRIDAY; el producto actual es una aplicación experimental con Windows como plataforma prioritaria, que ofrece chat escrito mientras se configura la voz.

**El modelo propone; la capa de políticas de Odessy decide.** El servicio valida las acciones, obtiene la aprobación humana requerida y vuelve a comprobar la autoridad antes de despachar las herramientas.

**Buscamos de 3 a 5 colaboradores de desarrollo** que quieran ejecutar un flujo de trabajo real, informar lo que falla y asumir un área delimitada. Empezar por el [manual de escritorio](docs/es/GOLDEN_PATH.md), elegir un [issue abierto de GitHub](https://github.com/Trisoma/odessy/issues) y leer la [ruta de contribución y responsabilidad de un área](docs/es/CONTRIBUTING.md#ruta-hacia-la-responsabilidad-de-un-área).

[Ejecutar desde el código fuente](docs/es/getting-started.md) · [Arquitectura](docs/es/ARCHITECTURE.md) · [Capturas de pantalla](docs/view/README.md) (solo en inglés) · [Soporte y límites](docs/es/current-status.md)

## Apuestas de arquitectura

- **La política tiene la autoridad.** La salida del modelo es una propuesta. Python posee la política y las aprobaciones; los adaptadores de herramientas vuelven a validar en el momento del despacho. Un mensaje de chat o un dispositivo conectado no otorgan derechos.
- **Un coordinador, objetivos de ejecución separados.** Mantener el modelo en el portátil o en un proveedor elegido; seleccionar ejecución local, emparejada y autenticada, o por SSH aprobada explícitamente. El equipo SSH no necesita modelo. La integración Edge/LAN tiene un alcance experimental más estrecho, y la MCU/automatización del hogar sigue siendo una dirección para contribuir, no un soporte implementado.
- **La voz es una interfaz principal prevista.** STT, TTS y la escucha de palabra de activación comparten el ciclo de vida del agente y los límites de autoridad con la entrada escrita. La configuración del habla, la latencia y la compatibilidad de hardware todavía requieren trabajo; la aprobación hablada no es autenticación de identidad.

Estas son decisiones de diseño para desarrollar y probar, no afirmaciones de que otros agentes carezcan de aprobaciones, de que todos los proveedores sean locales ni de que Odessy sea un sandbox completo.

## Probar la Developer Preview

La experiencia habitual es **abrir Odessy → configurar un modelo en Settings → Models and connections (Configuración → Modelos y conexiones) → elegir un área de trabajo → conversar y revisar acciones**. El escritorio se encarga del arranque del backend y de la autenticación local. Los usuarios no ejecutan Python manualmente ni intercambian tokens bearer.

- **¿Se dispone de un candidato completo?** Seguir el [manual ilustrado](docs/es/GOLDEN_PATH.md). La instalación en Windows incluye su entorno de ejecución compatible y su mantenimiento versionado.
- **¿Compilar desde el código fuente?** Seguir [Primeros pasos](docs/es/getting-started.md). Su modo gestionado por el escritorio usa el mismo ciclo de vida del servicio configurado, tras instalar los SDK de desarrollo. Los comandos de servidor manual y de modelo falso son comprobaciones separadas para colaboradores.

A fecha de 18 de noviembre de 2026, no hay publicado públicamente ningún instalador completo que coincida. Los archivos más antiguos [`v0.5.0-unstable` de cliente de interfaz](https://github.com/Trisoma/odessy/releases) no contienen la aplicación completa actual. Esta brecha de distribución y la configuración de las herramientas de compilación de Windows hacen que la incorporación sea más difícil de lo que debería. Consultar la [evidencia instalada](docs/verification/ssh-voice-installed-update-2026-11-18.md) (solo en inglés) para el candidato específico ejercitado; no califica todas las compilaciones posteriores.

## Qué se puede explorar

| Área | Comportamiento en la Developer Preview |
| --- | --- |
| Conversaciones | Proyectos, historial guardado, búsqueda, exportación, cambio de nombre, fijación y archivado. Custom admite una continuación acotada tras un reinicio; el historial de Harness es de solo lectura después del reinicio. |
| Herramientas y permisos | Acciones revisadas, aprobaciones explícitas, cancelación y modos de acceso compatibles de Custom. El control total nunca anula las denegaciones duras ni amplía una concesión existente. |
| Paneles del área de trabajo | Lecturas de archivos con alcance, diferencias propuestas y salida de comandos registrada. La salida es distinta de una terminal interactiva. |
| Contexto | Memoria de proyecto explícita y recuperación de documentos locales con adhesión voluntaria (opt-in), con citas de las fuentes y preparación acotada del contexto de Custom. |
| Terminal local | Compatibilidad condicional con la PTY de Windows cuando el conjunto verificado de componentes auxiliares nativos está disponible; requiere una concesión explícita de shell. No hay terminal SSH. |
| Dispositivos y SSH | Monitoreo de solo lectura más comandos SSH de Custom seleccionados por separado, cada uno con aprobación exacta. Iniciar sesión por sí solo no otorga ejecución ni acceso al área de trabajo; la LAN experimental es una ruta aparte. |
| Voz y configuración | Configuración existente de voz y de modelos, ocho grupos de configuración y preferencias de apariencia locales. El comportamiento del audio físico y de los proveedores necesita validación por separado. |

La creación, el listado y la vista previa de puntos de control siguen disponibles en Windows, pero **la restauración de puntos de control está deshabilitada en Windows** hasta que se implemente la seguridad de los identificadores de directorio. El backend rechaza las solicitudes directas de restauración; el escritorio explica la restricción. La restauración compatible en sistemas que no son Windows sigue requiriendo aprobación exacta. Consultar [límites de terminal y puntos de control](docs/ui/terminal-checkpoints.md) (solo en inglés).

## Alcance de plataformas

Windows x64 es la plataforma principal de desarrollo y de pruebas nativas registradas. Linux tiene cobertura de código fuente/CI y evidencia histórica acotada de dispositivos; eso no equivale a una paridad completa de escritorio/paquetes. macOS no está calificado. No se han establecido los requisitos de hardware. Leer la [matriz de soporte](docs/es/current-status.md) antes de elegir un despliegue.

## Seguridad y privacidad

Python posee la política y la autorización; Node posee la ejecución existente de herramientas MCP; Rust posee la identidad/transporte emparejado; Go agrega la telemetría opcional; Flutter usa clientes tipados. Seleccionar un modelo en la nube envía los datos de la solicitud a ese proveedor. La ocultación de datos sensibles se realiza en la medida de lo posible; no garantiza que no se divulgue información.

Un shell interactivo aprobado se ejecuta con los permisos del sistema operativo del usuario y no es un sandbox del área de trabajo por comando. La ejecución LAN heredada en texto plano no es apta para redes no confiables. Preferir las rutas de transporte autenticadas documentadas. Reportar las vulnerabilidades de forma privada mediante [SECURITY.md](SECURITY.md) (solo en inglés).

## Construir Odessy con nosotros

Somos un equipo pequeño de dos colaboradores habituales, con otras tres personas que ayudan de forma temporal, y nos encantaría tener compañía. Ya sea para corregir un error, mejorar un componente o trabajar con nosotros en una parte más amplia de Odessy, la participación es bienvenida. Buscamos colaboradores capaces de llevar una tarea concreta desde la reproducción hasta la implementación y la revisión. Las reproducciones, las pruebas y la documentación son primeras contribuciones útiles.

Algunas áreas en las que agradecemos la ayuda:

- **Agentes de IA:** orquestación, invocación de herramientas, integración de modelos y memoria.
- **Exploración de hardware:** Jetson, Raspberry Pi, BLE y comunicación con MCU. Son áreas de interés, no afirmaciones de soporte actual de dispositivos.
- **Sistemas:** Rust, redes, mTLS y ejecución segura.
- **Escritorio:** Flutter, Dart, accesibilidad y UI/UX.
- **Infraestructura:** Go, monitoreo, telemetría y gestión de múltiples equipos.
- **Voz:** STT, TTS, detección de palabra de activación y procesamiento de audio.

La documentación, las pruebas de compatibilidad y los informes de errores reproducibles también son bienvenidos. Odessy es un proyecto independiente impulsado por voluntarios. Las contribuciones no se remuneran y no hay un compromiso de tiempo fijo: ayudar cuando se pueda.

Empezar por [diagnósticos de Piper](https://github.com/Trisoma/odessy/issues/69), [estado de la conexión SSH](https://github.com/Trisoma/odessy/issues/70), [resúmenes de benchmark de TTS](https://github.com/Trisoma/odessy/issues/71) o [UX de la salida registrada](https://github.com/Trisoma/odessy/issues/72). Cada issue de GitHub contiene el alcance, los criterios de aceptación y los comandos de prueba. Comentar en el issue para coordinar antes de empezar.

Empezar por [Contribuir](docs/es/CONTRIBUTING.md), explorar la [arquitectura](docs/es/ARCHITECTURE.md), revisar los [issues abiertos](https://github.com/Trisoma/odessy/issues) o proponer una idea. Para cambios más grandes, hablar del enfoque con nosotros antes de empezar. Las contribuciones asistidas por IA son bienvenidas; quienes contribuyen siguen siendo responsables de la revisión, las pruebas y la atribución.

Odessy se distribuye bajo la [licencia Apache-2.0](LICENSE) (solo en inglés). Los componentes incluidos y los recursos de modelos tienen sus propios términos; consultar los [avisos de terceros](THIRD-PARTY-NOTICES.md) (solo en inglés) y el [inventario de licencias](docs/reference/third-party-licenses.md) (solo en inglés).
