# Primeros pasos

[English](../getting-started.md) | [简体中文](../zh-CN/getting-started.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha · Windows 11 x64**

Abrir el escritorio, configurar un modelo en Settings (Configuración), elegir un espacio de trabajo desechable
y enviar una solicitud. El escritorio inicia y autentica su servicio local por ti.
El arranque manual del servicio de Python y la copia de tokens son **comprobaciones de integración avanzadas**,
no el flujo de trabajo normal del usuario. La CLI del módulo sigue existiendo para el desarrollo y los diagnósticos.

## Elegir tu ruta

- **Instalador de Windows:** el candidato del borrador incluye su runtime; el usuario final no necesita SDK de Python, Node ni Flutter. Seguir el [manual](./GOLDEN_PATH.md#1-instalar-y-abrir-odessy) para el checksum exacto, instalación, Piper/Kokoro y activación opcional. Falta la verificación final del mantenedor.
- **Código fuente:** usar los pasos de desarrollo siguientes. Requiere SDK y es una ruta distinta del instalador proporcionado. Esta documentación no publica una descarga; obtener el candidato del distribuidor o usar el código fuente. Los archivos UI antiguos no contienen la aplicación completa actual.

## Preparar una copia del código fuente en Windows

Instalar Git, Python 3.13 con el iniciador `py`, Node.js 22, Flutter 3.47.7 stable
y la carga de trabajo **Desktop development with C++** (Desarrollo de escritorio con C++) de Visual Studio con un Windows SDK.
Usar `flutter doctor -v` para comprobar la preparación de la compilación para Windows. No se necesita GPU ni modelo de voz
para el chat escrito. La instalación de dependencias usa acceso a la red.

En PowerShell, desde una carpeta principal de tu elección, usar una copia nueva del código fuente:

```powershell
git clone --branch develop --single-branch https://github.com/Trisoma/odessy.git odessy-preview
Set-Location odessy-preview
$previewRepo = (Get-Location).Path.Replace('\', '/')
$previewPython = "$previewRepo/.venv/Scripts/python.exe"
py -3.13 -m venv .venv
& $previewPython -m pip install -e ".[test,ui]"
Push-Location tools
npm.cmd ci --no-audit --no-fund
npm.cmd run build
Pop-Location
flutter doctor -v
git rev-parse HEAD
```

Detenerse si un comando falla. Guardar la revisión del código fuente impresa con cualquier informe de error.
No es necesario activar el entorno virtual ni cambiar la política de ejecución de PowerShell.
Rust y Go solo se necesitan al compilar sus componentes opcionales; no son
necesarios para empezar el ejercicio de chat escrito local.

## Iniciar desde la aplicación de escritorio

En esa **misma terminal**:

```powershell
$previewDefines = @(
    '--dart-define=ODESSY_LOCAL_DESKTOP=true'
    "--dart-define=ODESSY_DESKTOP_ROOT=$previewRepo"
    "--dart-define=ODESSY_DESKTOP_PYTHON=$previewPython"
    "--dart-define=ODESSY_SETUP_ROOT=$previewRepo"
    "--dart-define=ODESSY_SETUP_PYTHON=$previewPython"
)
Set-Location apps/desktop
flutter pub get
flutter run -d windows @previewDefines
```

Estas definiciones seleccionan `LocalDesktopApplication` en el `lib/main.dart` de producción y
vinculan tanto el propietario del servicio como el ayudante de configuración al Python de esta copia del código fuente. Un
`flutter run -d windows` simple selecciona en su lugar la superficie de cliente desconectada. Ninguna de las dos es
`--demo`; el modo gestionado debe informar de un fallo de arranque en lugar de sustituirlo por datos de prueba.

No se necesita una segunda terminal de backend, un token generado manualmente ni una clave de API en la línea de comandos.
Usar **Settings → Models and connections** (Configuración → Modelos y conexiones) para configurar tu proveedor y modelo, y la
credencial enmascarada. Guardar, seguir el paso indicado de aplicación o reconexión y usar
**Connect saved configuration** (Conectar la configuración guardada) si aún no está conectado. El [manual](./GOLDEN_PATH.md#2-configurar-deepseek)
recorre DeepSeek como un ejemplo probado; otro proveedor compatible es opcional.
Las solicitudes en la nube pueden generar cargos y envían las observaciones permitidas a ese proveedor.

Si se detecta una configuración anterior del código fuente, revisar su modelo y su espacio de trabajo
antes de conectar. El estado del conector y del entorno de ejecución de la vista previa usa `build/local-desktop/state`;
el escritorio también puede recordar un puntero a la configuración del código fuente en la configuración de Odessy
del usuario. Esta es una compilación desde una copia del código fuente, no una afirmación de aislamiento completo del perfil ni de
una actualización de instalador. Cerrar la aplicación apaga su servicio.

## Llegar a la meta

Elegir una carpeta desechable mediante **Workspaces** (Espacios de trabajo), guardar y aplicar cualquier aviso de reinicio
y después iniciar un chat **Custom**. Seguir el [ejercicio local de Deny → Approve once](./GOLDEN_PATH.md#3-ejecutar-un-comando-en-tu-portátil-windows)
del manual.
Comprobar la salida de herramienta real y el código de salida. Un saludo de datos de prueba o la afirmación de éxito del asistente
no demuestran que se ejecutara una herramienta real.

La voz y SSH son pasos siguientes opcionales. La configuración desde el código fuente no descarga sus recursos ni
compila los ayudantes opcionales de monitoreo y contraseñas. Consultar [componentes de voz](../setup/voice-components.md) (solo en inglés)
y [configuración de SSH](../setup/ssh-computers.md) (solo en inglés) para sus requisitos separados.

## Diagnosticar un inicio fallido

Empezar por el error visible en Settings (Configuración). Para un diagnóstico con la CLI del código fuente, volver a la
raíz del repositorio, apuntar doctor al perfil gestionado por el código fuente y seleccionar el backend
que hayas configurado, por ejemplo:

```powershell
Set-Location $previewRepo
$env:ODESSY_CONFIG_FILE = "$previewRepo/build/local-desktop/state/odessy.env"
& $previewPython -m odessy doctor --model-backend deepseek
```

La configuración seleccionada y las credenciales del modelo también tienen propietarios de configuración y de almacén seguro;
doctor no es una réplica completa del estado del escritorio en ejecución. Una clave de API de solo sesión
está deliberadamente ausente en otro proceso. No copiar una clave a un archivo de texto plano
para satisfacer a doctor. Un fallo predeterminado de Ollama sin relación no demuestra que el servicio de
DeepSeek configurado haya fallado. Doctor puede sondear los endpoints configurados o listar las herramientas configuradas;
no descarga modelos, no ejecuta una inferencia en la nube en vivo ni prueba audio físico.

Usar los [pasos de solución de problemas y de reporte saneado](./GOLDEN_PATH.md#solución-de-problemas-y-reporte) del manual.
Para pruebas deterministas de componentes o un servidor de API gestionado manualmente, consultar las
[comprobaciones avanzadas de desarrollo](./CONTRIBUTING.md#comprobaciones-avanzadas-de-componentes-y-api).
La ruta de CI y de código fuente para Linux sigue disponible allí; esta guía de Windows no
califica paquetes de escritorio para Linux/macOS.
