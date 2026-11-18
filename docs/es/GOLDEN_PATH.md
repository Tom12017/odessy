# Manual de escritorio de Odessy

[English](../GOLDEN_PATH.md) | [简体中文](../zh-CN/GOLDEN_PATH.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha · Windows 11**

**Primer éxito:** conectar un modelo real, denegar un comando local y después aprobar una solicitud nueva y verificar su salida de herramienta. Completar las secciones 1–3 en un solo portátil Windows. La voz, las palabras de activación y SSH son ejercicios opcionales después de esa meta; no son requisitos previos.

El modelo propone acciones; el servicio aplica la política y obtiene la aprobación requerida antes de la ejecución. Usar un espacio de trabajo desechable. El confinamiento en Windows es parcial, y las solicitudes en la nube y las observaciones de herramientas permitidas salen de tu equipo hacia el proveedor elegido.

**Actualizado el 18 de noviembre de 2026.** El instalador siguiente parte de `1834c1a` más los cambios Piper/setup sin confirmar registrados; el mantenedor confirmó la instalación. Consultar la [identidad y alcance de las pruebas](../verification/windows-piper-installer-2026-11-18.md) (solo en inglés). Las capturas existentes corresponden al código anterior (`7f3b925`); no califican todas las funciones nuevas ni el recorrido completo de un usuario externo.

Si esta ruta no funciona en tu caso, [abrir un issue](https://github.com/Trisoma/odessy/issues/new/choose) con la **salida de doctor saneada** y el paso que falló. Consultar [Solución de problemas y reporte](#solución-de-problemas-y-reporte).

## 1. Instalar y abrir Odessy

### Requisitos previos

- Windows 11 x64, una conexión a internet y una carpeta local desechable para los comandos.
- Para este recorrido, una cuenta de la API de DeepSeek con una clave de API activa, acceso al modelo elegido y crédito de API suficiente. El uso del proveedor puede generar cargos. No se necesita GPU, micrófono ni un segundo equipo.
- **Solo instalación desde el código fuente:** [Git](https://git-scm.com/downloads/win), Python 3.13 con el iniciador `py` de Windows, [Node.js 22](https://nodejs.org/en/download) y [Flutter 3.47.7 stable](https://docs.flutter.dev/install). Las compilaciones de Flutter para Windows requieren la carga de trabajo **Desktop development with C++** (Desarrollo de escritorio con C++) de Visual Studio y un Windows SDK; comprobarlo con `flutter doctor -v`. Los módulos nativos de Node también pueden necesitar esas herramientas de compilación. La instalación completa desde el código fuente es más grande que una instalación para el usuario final.

Elegir **una** ruta a continuación. Un candidato empaquetado incluye su entorno de ejecución compatible; sus usuarios no necesitan los SDK de desarrollo.

### A. Instalador proporcionado

El candidato Windows x64 **`Odessy-v0.5.0-alpha-windows-x64-setup.exe`** se ha recompilado y el mantenedor confirmó su instalación correcta el 18 de noviembre de 2026. Usar ese candidato con su suma de comprobación, proporcionado por el mantenedor o mediante la [página de versiones](https://github.com/Trisoma/odessy/releases). Esta documentación no publica el archivo; los antiguos archivos de UI `v0.5.0-unstable` no lo sustituyen. Si no se dispone del candidato correspondiente, usar la ruta B.

Comparar el SHA-256 del archivo descargado antes de abrirlo:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\Odessy-v0.5.0-alpha-windows-x64-setup.exe'
```

SHA-256 esperado para este candidato: `15063674bf944db7beae83fa4b55318aca831e47801db7d3828a41f6edf831ae`. Cada compilación posterior necesita su propia suma y registro. Consultar el [registro del candidato](../verification/windows-piper-installer-2026-11-18.md) (solo en inglés).

1. Abrir el EXE y elegir la carpeta de instalación. Mantener el coordinador con ejecución local predeterminado; los otros roles están en **Custom setup**. El usuario final no necesita los SDK de Python, Node ni Flutter.
2. Elegir **Piper (recommended for CPU)** o **Kokoro** en **Speech output engine**. Para instalar voz automáticamente, activar **Install voice components**. No se necesita una instalación previa de Piper: tras confirmar la instalación se descargan el motor fijado, una voz inglesa, sus metadatos, Whisper.cpp y las dependencias de audio. Revisar el tamaño y las licencias; estas descargas opcionales requieren internet.
3. Activar **Install the wake-word model** por separado si se desea. Su modelo tiene licencia CC BY-NC-SA 4.0. Se pueden omitir voz y activación para usar chat escrito. **Use existing voice components** permite seleccionar archivos existentes; no instala los que falten.
4. Revisar el plan y pulsar **Install**. Una caché completa puede mostrar cero bytes pendientes; el instalador todavía instala y verifica los paquetes en esta instalación. Esperar a que termine y elegir **Open Odessy**. Consultar [el asistente](../setup/wizard.md) y [los componentes de voz](../setup/voice-components.md) (solo en inglés).
5. Configurar el modelo como se describe abajo y elegir una carpeta desechable en **Workspaces**. Tras conectar el audio, probar STT/TTS y activar explícitamente la escucha de palabra de activación en Settings; instalar archivos no verifica el micrófono ni los altavoces.

Para actualizar una instalación versionada existente, elegir su ubicación registrada y revisar la actualización en **Manage installation**. Conservar el perfil y los modelos; no es necesario desinstalar primero. La detección y descarga automática de actualizaciones dentro de la app todavía no están implementadas.

![Diseño del chat con la barra de proyectos y el compositor](../view/conversation/projects-and-recent.png)

*Ejemplo de la galería. Las imágenes existentes de la galería y de SSH conservan su identidad de código original; no son capturas nuevas de este instalador.*

### B. Compilar el escritorio de producción desde el código fuente

Seguir [Primeros pasos](./getting-started.md) para conocer las dependencias exactas de Windows y el
**arranque del código fuente gestionado por el escritorio**. Este inicia el servicio configurado desde la aplicación;
no es necesario iniciar Python manualmente, copiar un token de portador ni introducir la clave de un proveedor en una terminal.
Después, volver a la sección 2. Los comandos manuales de servidor y de modelo falso pertenecen a las
comprobaciones avanzadas para colaboradores y no son necesarios para este recorrido.

## 2. Configurar DeepSeek

Elegir **Custom** como motor para los chats nuevos. Custom selecciona el motor del agente y DeepSeek aporta el modelo. La configuración del código fuente llama a este motor `legacy`; es el mismo motor Custom.

Tanto la aplicación instalada como el escritorio gestionado desde el código fuente configuran el modelo mediante
Settings (Configuración) y gestionan el ciclo de vida de su servicio. Guardar y seguir cualquier paso indicado de aplicación o
reinicio. Si el servicio no está conectado, usar **Connect saved configuration** (Conectar la configuración guardada);
no sustituirlo por el diálogo manual de token **Connect local service** (Conectar el servicio local).

1. En **Settings → Models and connections** (Configuración → Modelos y conexiones), elegir **DeepSeek**. Usar el endpoint predeterminado del proveedor (`https://api.deepseek.com/v1`) y seleccionar o introducir `deepseek-flash`, el ID de modelo registrado en la instalación del mantenedor.
2. Introducir tu clave de API de DeepSeek en el campo enmascarado. Elegir **Save securely** (Guardar de forma segura) o **Use for this session only** (Usar solo en esta sesión) y después guardar la configuración del modelo. Consultar [credenciales del modelo](../setup/secure-model-credentials.md) (solo en inglés).
3. Iniciar un chat Custom nuevo y escribir “Reply with one sentence confirming you can see this message.”; después, comprobar el modelo activo y esperar una respuesta. Si falla, comprobar el proveedor, el ID de modelo, el estado de la credencial y el error de conexión.

La API de DeepSeek es el ejemplo probado por el mantenedor en esta guía. Odessy también admite otros proveedores de API y modelos locales. Con recursos de prueba limitados, no hemos verificado manualmente esas configuraciones para este recorrido.

![Configuración de Models and connections](../view/settings/models-and-connections.png)

*Ejemplo de la galería de escritorio. Seleccionar el modelo y el proveedor en Models and connections (Modelos y conexiones).*

## 3. Ejecutar un comando en tu portátil Windows

Este es el ejercicio central de aprobación. Solo necesita tu portátil Windows. El comando `hostname` de Windows imprime el nombre de tu equipo, por ejemplo `MY-LAPTOP`, y después termina sin modificar archivos ni la configuración. Lo usamos porque su salida real de herramienta es fácil de comparar con PowerShell. `terminal.run` es la herramienta de Odessy para ejecutar ese comando; no es otro comando que necesites instalar. Mantener la ejecución en local; desconectar antes cualquier destino de ejecución SSH/LAN seleccionado. Seleccionar una carpeta desechable mediante **Workspaces** (Espacios de trabajo), guardar y seguir cualquier aviso de reinicio antes de crear el chat. Esto se aplica tanto a la aplicación instalada como a la aplicación gestionada desde el código fuente.

1. Iniciar un **chat Custom nuevo** con tu modelo real. En el menú del escudo del compositor (**Service permissions**, Permisos del servicio), seleccionar **Ask every time** (Preguntar cada vez). Esperar la confirmación del servicio; si el control informa de que no está disponible o muestra un error, detenerse. Las lecturas permitidas normales pueden ejecutarse sin solicitar confirmación; este ejercicio usa `hostname`, que la política predeterminada clasifica como sujeto a confirmación.
2. Enviar este prompt exacto:

   ```text
   Use terminal.run to run exactly hostname on this Windows laptop in the current workspace. Do not use SSH, substitute another command, or retry if I deny it. Show the tool's stdout and exit code.
   ```

3. Revisar la herramienta, los argumentos exactos y el destino de la aprobación. Debe ser `terminal.run` local con el comando `hostname` en el espacio de trabajo elegido. Seleccionar **Deny** (Denegar). Esperar un resultado denegado y ningún resultado de ejecución correcto para esa solicitud. Si el modelo propone una alternativa, denegarla y detener el turno en lugar de aprobar una acción diferente.
4. Enviar el mismo prompt como una **solicitud nueva**. Revisar su nueva aprobación y después elegir **Approve once** (Aprobar una vez). Si los argumentos o el destino difieren, denegar e investigar. Esta aprobación no concede acceso general a comandos posteriores.
5. Abrir el panel **Output** (Salida) del inspector mientras esta sesión en vivo está activa. Esperar que el resultado de `terminal.run` contenga un nombre de host no vacío y el código de salida `0`. Ejecutar `hostname` tú mismo en PowerShell y comparar los nombres. Una frase del asistente diciendo que funcionó no es suficiente.

**Línea de meta:** un modelo real respondió, una solicitud local fue denegada, una solicitud aprobada por separado devolvió una salida de herramienta coincidente y el destino local estaba claro. Puedes detenerte aquí e informar de tu resultado; los ejercicios restantes son opcionales.

Con la política predeterminada, la comprobación sin ejecución siguiente informa `decision: confirm` y `asks: true`. Ejecutarla desde tu espacio de trabajo desechable con el Python del entorno del código fuente si la interfaz omite inesperadamente la aprobación:

```powershell
$previewPython = 'C:\path\to\odessy-preview\.venv\Scripts\python.exe'
& $previewPython -m odessy permissions check 'hostname' --json
```

Sustituye `C:\path\to\odessy-preview` por la ruta real de tu copia del código fuente. Este diagnóstico opcional necesita su entorno de Python; si solo usas la aplicación instalada, puedes informar de la aprobación y de Output que muestra la interfaz.

Esta comprobación nunca ejecuta `hostname` y no anula el modo en vivo, las reglas personalizadas, los hooks ni las preaprobaciones guardadas. **Ask every time** no significa que toda lectura inofensiva solicite confirmación. Si tu configuración es distinta, informa de ello; no debilitar la política para forzar que este ejercicio pase.

[![Chat instalado en Windows con resultados de terminal.run en Output](../view/main/basic-chat.png)](../view/main/basic-chat.png)

*Vista previa instalada en Windows: Output (Salida) muestra los resultados subyacentes de `terminal.run`. Este intercambio registrado enumera archivos del espacio de trabajo y de Desktop; no es una captura del ejercicio `hostname` anterior. Una búsqueda de la ruta de Desktop falló con código de salida `1`; un comando posterior resolvió la ruta redirigida de Desktop y terminó con código de salida `0`. Comprobar cada resultado de herramienta en lugar de confiar solo en la respuesta del asistente.*

## 4. Opcional: configurar la voz y la palabra de activación

Configurar componentes de voz compatibles en la aplicación instalada o en la aplicación gestionada desde el código fuente antes de este ejercicio. Las dependencias de compilación del código fuente no incluyen los modelos de voz ni todas las dependencias de audio; seguir [Componentes de voz](../setup/voice-components.md) (solo en inglés). El arranque gestionado desde el código fuente usa el ciclo de vida de voz configurado, mientras que un servidor de API manual iniciado por separado puede omitirlo.

1. En **Settings** (Configuración), abrir **Speech to text** (Voz a texto), **Text to speech** (Texto a voz) y **Voice** (Voz) para elegir tus componentes de voz compatibles, el micrófono y el dispositivo de salida. Guardar los cambios. Si se pide proporcionar o descargar recursos, seguir [Componentes de voz](../setup/voice-components.md) (solo en inglés). Los modelos de activación son una opción separada (opt-in).
2. Abrir **Voice options → Test speech output** (Opciones de voz → Probar la salida de voz) en el compositor. Después elegir **Test speech input · no model call** (Probar la entrada de voz · sin llamada al modelo) y decir una frase corta. Comprobar la reproducción y la transcripción por separado.
3. Probar push-to-talk (pulsar para hablar). Después habilitar la escucha de activación. Con el modelo Jarvis incluido, decir **“Hey Jarvis”**, esperar la señal de escucha y hacer una pregunta corta.
4. Detener la escucha de activación desde los controles de voz antes de cambiar de dispositivo de audio. Si un cambio de configuración se aplaza, terminar la operación de audio en curso y comprobar que el cambio se aplica cuando el audio está inactivo.

![Configuración del reconocimiento de voz](../view/settings/speech-to-text.png)

![Configuración de voz](../view/settings/voice.png)

*Ejemplos de la galería de escritorio. El reconocimiento de voz configura la transcripción. La configuración de Voice (Voz) controla el comportamiento de escucha.*

Si no hay transcripción, empezar por el micrófono y la prueba de entrada. Si el texto llega despacio después de que aparezca una transcripción, comprobar la respuesta del modelo. Si el texto aparece antes que el habla, comprobar la síntesis y el altavoz seleccionado. La voz puede resultar lenta en la configuración probada. Incluir la etapa en la que observaste el retraso al informar de ello.

## 5. Opcional: ejecutar un comando en otro equipo mediante SSH

Como en el ejercicio local, `hostname` imprime el nombre del equipo seleccionado. Aquí el comando se ejecuta en el equipo SSH en lugar de tu portátil Windows. El ejemplo de configuración desarrollado es un **Jetson Orin Nano Super**. Usar tu propio equipo SSH accesible con un shell POSIX y una cuenta en la que ya puedas iniciar sesión. Las direcciones de conexión se omiten en esta guía y se ocultan en las capturas.

1. En **Devices → Connect a computer** (Dispositivos → Conectar un equipo), introducir un alias SSH o `user@hostname`. Rellenar el puerto si es necesario. Dejar la contraseña en blanco para usar tu clave o agente SSH configurados. Verificar la clave del host de forma independiente y seguir las [instrucciones de confianza de SSH](../setup/ssh-computers.md) (solo en inglés) si es desconocida o ha cambiado.

   ![Página de conexión SSH de Odessy instalada tras un inicio de sesión correcto, con los detalles privados de conexión pixelados](../view/manual-ssh-live/01-ssh-connected.png)

   *Ventana real de Odessy instalada tras iniciar sesión en el equipo Debian del mantenedor. La dirección, el puerto y el ejemplo de ayuda de dirección están pixelados por privacidad. El campo de contraseña está vacío. Usar tus propios detalles de conexión.*

2. Seleccionar **Connect** (Conectar). El inicio de sesión comienza con un monitoreo de solo lectura. Abrir **Devices → Overview** (Dispositivos → Resumen) para encontrar el equipo conectado y su nombre de host detectado. Comprobar la frescura del monitoreo por separado del estado de inicio de sesión.

   ![Resumen de Devices de Odessy instalada que muestra localhost en línea mediante SSH](../view/manual-ssh-live/02-devices-overview.png)

   *Resumen real de Devices (Dispositivos). El equipo Debian conectado informa el nombre de host `localhost` y aparece en línea con monitoreo SSH de solo lectura. La tarjeta `jetson` separada es una entrada guardada, no el equipo conectado en esta captura. La identidad de la conexión está pixelada.*

3. Volver a **Connect a computer** (Conectar un equipo). Solo con iniciar sesión no se habilitan los comandos del agente: el estado siguiente muestra **Agent commands · not selected** (Comandos del agente · no seleccionado). Desplazarse hasta **Use for agent commands** (Usar para comandos del agente) y seleccionarlo por separado. Esto abre un chat Custom nuevo con la herramienta SSH disponible.

   ![Estado SSH de solo lectura de Odessy instalada y el botón separado Use for agent commands](../view/manual-ssh-live/03-enable-agent-commands.png)

   *Ventana real de Odessy instalada, desplazada para mostrar **Use for agent commands**. El inicio de sesión y el transporte están verificados; la sesión está en línea y lista, mientras que los comandos del agente siguen **not selected** (no seleccionados). Esta captura es anterior al acceso a comandos. Los detalles privados de la conexión están pixelados.*

4. En el chat nuevo, escribir **“On the selected SSH computer, run `hostname` using `ssh.run`.”** Comprobar el comando y el destino exactos en la aprobación y rechazarla una vez. Confirmar que no hay un resultado remoto correcto para esa solicitud. Volver a preguntar, revisar la aprobación y aprobar una vez. Comprobar la salida de herramienta devuelta y el código de salida en el panel **Output** (Salida) del chat activo.
5. Comparar los dos ejercicios: `hostname` en local debería devolver el nombre de tu portátil Windows; `hostname` en remoto debería devolver el nombre del equipo SSH seleccionado. Seleccionar **Disconnect agent commands** (Desconectar los comandos del agente) al terminar.

El intercambio SSH guardado del mantenedor provino de un **equipo Debian x86-64 separado**, no del ejemplo de configuración de Jetson. Su resultado `ssh.run` registrado fue:

```text
stdout: localhost
exit code: 0
```

Este es un extracto de texto del resultado de herramienta confirmado, no una captura del resultado del comando. `localhost` era el nombre de host configurado de ese equipo Debian; no significa que el comando SSH se ejecutara en el coordinador de Windows. En tu propio host, comparar con `hostname` en una sesión SSH independiente.

Al reabrir el chat SSH guardado, la respuesta del asistente era visible, pero el panel **Output** (Salida) de la sesión reanudada estaba vacío. No se guardó ninguna captura en vivo de la salida de herramienta SSH. Las capturas reales de conexión y de Devices (Dispositivos) anteriores establecen el inicio de sesión y el estado de conexión; no muestran la ejecución de comandos. Para los ejercicios, inspeccionar Output mientras la sesión en vivo del comando está activa.

Las capturas SSH de ventana completa se tomaron de la aplicación instalada el **18 de noviembre de 2026**. La identidad del ejecutable instalado, las ediciones de privacidad y los límites de la evidencia están registrados en el [manifiesto de capturas](../view/manual-ssh-live/manifest.json) (solo en inglés).

El flujo SSH actual tiene varios pasos manuales. El monitoreo y la selección de comandos tienen controles separados, habilitar los comandos inicia un chat nuevo y reiniciar el servicio exige volver a conectar. Los comandos se ejecutan con los permisos de la cuenta SSH y sin sandbox remoto. Usar el destino que se muestra en la aprobación para distinguir un comando remoto de un comando del portátil. La [guía de SSH](../setup/ssh-computers.md) (solo en inglés) cubre la pérdida de conexión y los destinos compatibles.

## 6. Opcional: explorar el escritorio

| Dónde | Qué probar |
| --- | --- |
| **Projects and history** (Proyectos e historial) | Crear o cambiar de proyecto, abrir un chat guardado, buscar en el historial o usar el menú del chat para renombrar, fijar, archivar o exportar. Custom admite una continuación acotada tras un reinicio. El historial de reinicio de Harness es de solo lectura. |
| **Composer** (Compositor) | Cambiar el modelo para el siguiente turno. Abrir los permisos del servicio y comprobar el modo efectivo. Los comandos SSH siguen requiriendo aprobación explícita. |
| **Inspector** | Explorar **Files** (Archivos) del espacio de trabajo, **Output** (Salida) registrado y **Changes** (Cambios). Un **Terminal** interactivo disponible usa una concesión de shell separada y se ejecuta bajo tu cuenta del sistema operativo. [Terminal y puntos de control](../ui/terminal-checkpoints.md) (solo en inglés) |
| **Context, memory and documents** (Contexto, memoria y documentos) | Inspeccionar el contexto usado por un turno, revisar la memoria del proyecto o habilitar la indexación de documentos y seguir las citas de recuperación. La disponibilidad depende del motor y de la configuración. |
| **Checkpoints** (Puntos de control) | Revisar o previsualizar los puntos de control registrados del espacio de trabajo. Windows admite la creación, el listado y la vista previa de puntos de control. La restauración está deshabilitada. |
| **Activity & usage** (Actividad y uso) | Comprobar la actividad registrada y el uso de modelos de esta instalación. |
| **Devices, Jobs and Handoffs** (Dispositivos, trabajos y traspasos) | Comprobar los hosts disponibles y después inspeccionar los trabajos o traspasos registrados cuando la funcionalidad correspondiente tenga actividad. |
| **Settings** (Configuración) | Explorar la apariencia general, los modelos y las conexiones, la voz a texto, el texto a voz, la voz, los dispositivos y el acceso a herramientas, la configuración avanzada y el mantenimiento de la instalación. |

[Explorar la galería ilustrada del escritorio](../view/README.md) (solo en inglés) · [Limitaciones actuales](./LIMITATION.md)

## Solución de problemas y reporte

Estas son limitaciones conocidas y puntos de fallo probables en este recorrido. Las [limitaciones completas](./LIMITATION.md) también cubren capacidades fuera de la ruta principal.

| Síntoma o límite | Qué hacer |
| --- | --- |
| No hay una descarga de instalador que corresponda | Usar la ruta B del código fuente. Los archivos empaquetados antiguos del cliente de interfaz no son un sustituto completo de la aplicación y el servicio actuales. |
| Falla la preparación de Python, npm o Flutter | Comprobar los requisitos previos, el iniciador de Python 3.13, Node 22 y `flutter doctor -v`. Las herramientas de C++ de Windows son necesarias para las compilaciones nativas. No continuar después de que falle un comando de dependencia o de compilación. |
| Falla el arranque, se rechaza la conexión o aparece HTTP 401 | En la aplicación gestionada, inspeccionar el error de arranque y la configuración guardada y después reintentar **Connect saved configuration** (Conectar la configuración guardada). Es la dueña de su propio puerto y de su token. Las compilaciones desde el código fuente necesitan todas las definiciones del arranque gestionado. Solo una conexión de API deliberadamente manual usa puertos y tokens introducidos por el operador. |
| El modelo informa errores de autenticación, de modelo no encontrado, de límite de velocidad o de crédito | Comprobar el endpoint del proveedor, el ID de modelo actual y el acceso o crédito de la cuenta. Que doctor encuentre una clave no la valida en línea. Informar del error del proveedor sin la clave. No suponer que una solicitud fallida fue gratuita. |
| Falla el guardado seguro de la clave | Usar deliberadamente **Use for this session only** (Usar solo en esta sesión) o reparar el backend de credenciales del sistema operativo compatible. Ambas rutas de arranque gestionado pasan las credenciales de sesión de forma privada; guardar una clave en texto plano no es una solución alternativa. |
| No aparece ninguna aprobación, o aparece un comando o destino diferente | Comprobar Custom, el **Ask every time** (Preguntar cada vez) efectivo, el destino local, el espacio de trabajo seleccionado y cualquier preaprobación o hook de comandos guardados. Denegar las solicitudes que no coincidan; inspeccionar la comprobación de política sin ejecución anterior. Ni un panel ni una selección de modo conceden nuevos derechos sobre el espacio de trabajo. |
| Se vuelve a proponer un comando denegado | La denegación no ejecuta esa propuesta. Detener el turno e informar de la propuesta repetida; no aprobarla solo para que la interfaz avance. |
| El comando falla o el código de salida no es cero | Leer el Output real y los argumentos de la aprobación. Comprobar la validez del espacio de trabajo y la preparación del shell o la herramienta. No deshabilitar el confinamiento ni usar el control total como solución alternativa de configuración. El confinamiento en Windows sigue siendo parcial incluso cuando el comando se ejecuta correctamente. |
| La salida está vacía tras reabrir el historial | El mantenedor observó un panel Output vacío en la sesión SSH reanudada. Inspeccionar y capturar el resultado de herramienta en vivo antes de cerrar el chat; no volver a ejecutar una acción solo para recrear la evidencia. El historial y la prosa del asistente no son prueba de una nueva ejecución. |
| Un chat guardado no puede continuar | Usar el perfil y el espacio de trabajo correspondientes. La continuación de Custom es acotada; el historial de reinicio de Harness es de solo lectura. No eliminar la base de datos del historial para reparar la selección. |
| La voz opcional o Devices (Dispositivos) no está disponible | El chat local escrito no necesita ninguna de las dos funcionalidades. Comprobar el dispositivo de audio seleccionado y las pruebas individuales de STT/TTS; el inicio de sesión SSH, la preparación del monitoreo y la autorización de comandos son independientes. Volver a conectar las sesiones SSH temporales después de reiniciar el servicio. |
| Una acción en la nube o de shell expone datos | Las solicitudes en la nube y las observaciones de herramientas permitidas se envían al proveedor configurado. Las acciones de shell tienen los permisos documentados del host; las aprobaciones no son un sandbox completo del sistema operativo. Usar datos desechables y no sensibles. La restauración de puntos de control en Windows está deshabilitada y no es una reversión para los comandos ejecutados. |

### Recopilar diagnósticos

Para la **ruta B del código fuente**, conservar el error visible de arranque o de modelo y la revisión del código fuente.
Desde la raíz del repositorio, en una terminal de desarrollo separada, usar el Python y el perfil gestionado por el código fuente
de la misma copia para un diagnóstico complementario:

```powershell
$previewRepo = (Get-Location).Path.Replace('\', '/')
$previewPython = "$previewRepo/.venv/Scripts/python.exe"
$env:ODESSY_CONFIG_FILE = "$previewRepo/build/local-desktop/state/odessy.env"
& $previewPython -m odessy doctor --model-backend deepseek 2>&1 |
    Tee-Object -FilePath "$previewRepo/build/local-desktop/doctor.txt"
```

Sustituir `deepseek` por el backend que hayas configurado. Añadir `--voice` solo al diagnosticar
el ejercicio opcional de activación y voz. Doctor comprueba la configuración de un proceso y las
herramientas disponibles; una clave de solo sesión del escritorio no se hereda deliberadamente en esta
terminal separada. No verifica por completo la configuración del escritorio seleccionada,
la inferencia del proveedor, la compatibilidad con Piper ni el audio físico. Registrar esa limitación
en lugar de poner credenciales en un archivo para que doctor pase. Puede sondear los endpoints configurados
o listar las herramientas configuradas; no descarga modelos.

Para un **candidato instalado**, recopilar los resultados de **Settings → Manage installation → Check installed files**
(Configuración → Gestionar la instalación → Comprobar los archivos instalados) y su identidad de compilación y versión. Si también
ejecutas doctor, usar el intérprete y el perfil propios de ese candidato, no un Python del sistema o una copia del código fuente
que no tengan relación. Si no puedes localizarlos, informar de la comprobación de instalación y solicitar el comando de diagnóstico
correspondiente; no adivinar otro entorno de ejecución ni reinstalar primero.

Leer el informe antes de compartirlo. Eliminar las claves de API, los tokens de portador, las URL que contienen credenciales,
las direcciones y nombres de cuenta privados, las rutas sensibles y cualquier contenido privado de herramientas o archivos.
La ocultación de datos sensibles no garantiza que no se divulgue información; nunca adjuntar tu entorno, los archivos de perfil ni la base de datos del historial como sustituto.

[Abrir un issue con diagnósticos saneados](https://github.com/Trisoma/odessy/issues/new/choose), incluido:

- Ruta de instalación, revisión del código fuente o de la compilación y versión de Windows.
- El paso numerado exacto, el resultado esperado y el error observado.
- Salida de doctor saneada (o la comprobación de archivos instalados cuando doctor no esté disponible).
- Para el ejercicio central, si Deny (Denegar) impidió la ejecución y si Approve once (Aprobar una vez) produjo una salida de `hostname` coincidente con código de salida `0`.

## Ayuda a mejorar la parte que acabas de probar

- **Verificar otro modelo.** Probar otro proveedor de API o un modelo local e informar de la configuración exacta y del primer turno correcto. Empezar por el [registro de proveedores](../../src/odessy/model_providers.py) (solo en inglés) y la [prueba de ida y vuelta del modelo de escritorio](../../tests/test_desktop_cloud_roundtrip.py) (solo en inglés).
- **Medir un turno de voz lento.** Registrar el dispositivo, el modelo y dónde notaste el retraso. Empezar por el [rendimiento de voz](../ui/voice-performance.md) (solo en inglés) y las [pruebas de audio híbrido](../../tests/test_hybrid_audio.py) (solo en inglés).
- **Mejorar la incorporación de SSH.** Intentar conectar un dispositivo desde un perfil nuevo e identificar el paso que dificultó saber si los comandos estaban habilitados. Empezar por el [controlador de conexión SSH](../../apps/desktop/lib/app/ssh_connection_controller.dart) (solo en inglés) y las [pruebas de interfaz de ejecución SSH](../../apps/desktop/test/ssh_execution_test.dart) (solo en inglés).

Para un primer PR centrado, elegir un [issue abierto de GitHub](https://github.com/Trisoma/odessy/issues) y comentar el alcance propuesto. Los issues incluyen archivos, criterios de aceptación y comprobaciones. Consultar [Contribuir](./CONTRIBUTING.md#ruta-hacia-la-responsabilidad-de-un-área) para conocer la revisión y la responsabilidad continuada de un área.
