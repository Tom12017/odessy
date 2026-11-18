# Estado actual de soporte y de la versión

[English](../current-status.md) | [简体中文](../zh-CN/current-status.md) | **Español**

> Nota: la versión en inglés es la versión canónica; esta traducción es solo de referencia. Las capturas muestran la interfaz en inglés; la aplicación aún no está localizada.

**Developer Preview · v0.5.0-alpha**
Documentación revisada: 19 de noviembre de 2026 (trabajo de publicación del día 18).

## Base de código fuente y de versión

El candidato Windows x64 del borrador se compiló desde el código confirmado `6f96e71c0d1517030bf30729546d4bb90578bdc3` en `fix/windows-setup-long-paths`. El [registro del candidato](../verification/windows-piper-installer-2026-11-18.md) (solo en inglés) identifica el checksum y las dependencias reutilizadas y verificadas mediante hash. Los commits posteriores solo de documentación no cambian la identidad del código de la aplicación.

Falta la verificación humana final de este candidato recompilado. Las comprobaciones automáticas incluyen 131 pruebas Python afectadas, 68 widgets de instalación y gestión, análisis Flutter limpio, 107 contratos y una base Piper instalada previamente. La actualización/reparación aislada del código final pasó: Piper generó audio, se conservaron dispositivos/modelo/espacio de trabajo y archivos de prueba, y coincidieron los hashes del código instalado. El CI alojado pasó en `6f96e71`, incluidas las suites completas Python/escritorio y la instalación nativa sin conexión. La aceptación del instalador anterior del 18 de noviembre sigue siendo histórica y solo corresponde a su hash original.

El error `ssh -G failed` procedía del script de verificación, que omitía la variable Windows `ProgramData`. Tras corregir el entorno de arranque, la misma app instalada pasó la inspección SSH autenticada y el mantenedor confirmó el acceso. No se reemplazaron archivos de la app ni el instalador. Siete casos nuevos comprueban la preservación del entorno del sistema/perfil; pasan 52 pruebas de arranque Windows, servicio instalado y SSH.

La etiqueta pública sigue siendo **v0.5.0-alpha**. Se prepara un borrador de preversión sin publicar para la verificación del mantenedor; no debe publicarse automáticamente. Firma y aceptación en máquina limpia, hardware y proveedores siguen siendo verificaciones separadas. Las capturas y el [registro anterior](../verification/ssh-voice-installed-update-2026-11-18.md) (solo en inglés) conservan sus identidades originales.

## Primera ejecución de un colaborador

El flujo de trabajo instalado normal es **abrir la app → Settings (Configuración) → modelo/espacio de trabajo → chat**.
El escritorio inicia su servicio autenticado; no se necesita una terminal backend operada por el usuario.
La [configuración desde el código fuente](./getting-started.md) usa el mismo ciclo de vida gestionado tras
instalar los SDK de desarrollo. El modelo ficticio de la CLI y el intercambio manual de tokens son
comprobaciones separadas de componente/API, no la ruta principal de incorporación del producto.

[Abre issues en GitHub](https://github.com/Trisoma/odessy/issues) y la [ruta hacia la responsabilidad de un área](./CONTRIBUTING.md#ruta-hacia-la-responsabilidad-de-un-área)
ofrecen rutas concretas de contribución. No prueban el éxito de la incorporación externa, los tiempos de
respuesta de los mantenedores ni una concesión de permisos a colaboradores. El tiempo de la primera ejecución
y la aceptación del camino dorado por parte de un lector externo siguen sin medirse.

## Matriz de capacidades

| Capacidad | Alcance implementado | Límite importante |
| --- | --- | --- |
| Escritorio | Shell Flutter de producción, proyectos/chats recientes, inspector, Activity & usage (Actividad y uso), Jobs, Handoffs y ocho grupos de ajustes | Una página visible no garantiza que su capacidad de backend esté disponible. |
| Historial duradero | Proyectos/conversaciones/eventos SQLite locales al perfil, búsqueda y exportación acotada | La navegación del historial no tiene efectos secundarios; las llamadas almacenadas no se reproducen. |
| Continuación de Custom | Restaura los intercambios públicos completados en un controlador autorizado nuevo | El vínculo con el espacio de trabajo debe coincidir; las concesiones, aprobaciones, trabajos y handles de proceso no se restauran. |
| Harness | Runtime seleccionable e historial legible guardado | La continuación tras reiniciar y la paridad de modos de acceso/contexto de Custom no están disponibles; sin respaldo silencioso. |
| Modos de acceso | Custom ask/auto/full con acuses de recibo del servicio y revisiones | La política existente, las denegaciones duras, las rutas sensibles y las concesiones independientes siguen vigentes. |
| Contexto/memoria/recuperación | Hechos de proyecto explícitos, indexación léxica acotada con activación opt-in y contexto/citas de Custom | Siguen siendo necesarias la validación de fuentes y la autoridad actual del espacio de trabajo en vivo. Sin indexación automática en la nube. |
| Terminal interactiva | PTY local de Windows con helper Node/nativo empaquetado verificado y concesión explícita | Se ejecuta con los permisos del sistema operativo del usuario; sin PTY remoto, handles restaurados ni entrada reproducida. Sin el conjunto completo de componentes necesarios, no está disponible. |
| Checkpoints | Instantáneas de texto acotadas y vista previa respaldadas por Git; la restauración compatible fuera de Windows usa aprobación exacta y una instantánea de seguridad | La restauración en Windows está deshabilitada en el servicio y en la UI a la espera de una seguridad basada en handles. La creación, el listado y la vista previa siguen disponibles; los archivos binarios/sensibles/no compatibles quedan excluidos. |
| Monitorización | Agregación opcional en Go con telemetría local/emparejada y estado SSH de solo lectura | La conectividad, el permiso y la frescura de los datos siguen siendo independientes. Los DTO de monitorización no conceden acceso de ejecución ni de espacio de trabajo. |
| Ejecución SSH | Selección explícita de un destino Custom temporal y comandos `ssh.run` aprobados exactamente | Separada de la monitorización; sin sandbox remoto, PTY, inspector de archivos ni ejecución SSH de Harness. Reconecta tras reiniciar el servicio. |
| Voz | Piper recomendado para CPU; Kokoro seleccionable; Whisper y descarga de activación por voz opcionales | Carga/síntesis Piper instalada verificada; micrófono, reproducción, eco y activación necesitan aceptación por dispositivo. |
| Configuración (Setup) | Instalador Windows con runtime privado, mantenimiento versionado e instalación Piper/Kokoro opcional | El borrador recompilado espera verificación humana final; firma, hardware amplio y máquina limpia siguen siendo verificaciones separadas. |

## Matriz de plataformas

| Plataforma | Evidencia y nivel de soporte |
| --- | --- |
| Windows x64 | Objetivo principal de la Developer Preview; existen código fuente/CI y comprobaciones nativas/instaladas registradas para instantáneas concretas. La calificación del candidato final sigue siendo independiente. |
| Linux x86_64 | Cobertura de código fuente/CI; el empaquetado portátil y la aceptación de la GUI nativa no están establecidos para la instantánea final. |
| Jetson/Linux ARM64 | Solo evidencia histórica de monitorización, emparejamiento y voz específica de esa dirección. No es una afirmación general sobre escritorio ni sobre ejecución. |
| macOS | No calificado. |

No se afirma ninguna especificación mínima general de RAM/GPU, un sandbox completo, paridad de
coordinación autónoma ni soporte de MCU. La ejecución de comandos SSH tiene el alcance acotado de Custom
descrito arriba; no es un IDE remoto general ni una garantía de confinamiento.

## Puertas de control antes de una afirmación de beta

1. Mantén deshabilitada la restauración de checkpoints en Windows en el candidato de versión hasta que
   se verifique la protección basada en handles. Resuelve o deshabilita cualquier otro hallazgo de seguridad/pérdida de datos.
2. Compila y audita un candidato coherente a partir de la instantánea final del código fuente con
   conjunto de versiones fijadas del runtime, los componentes auxiliares y sus dependencias, licencias y hashes de artefactos.
3. Verifica la instalación/actualización/desinstalación aisladas y la preservación de perfil/historial/ajustes
   contra ese candidato; distingue los fixtures de la evidencia real de la bóveda de credenciales/el proveedor.
4. Haz coincidir la incorporación, los flujos de trabajo compatibles, las capturas y las limitaciones con el candidato.
5. Registra la aceptación visual de los mantenedores y las puertas restantes de plataforma/hardware/proveedor.

Alpha no exime de los requisitos de seguridad. No distribuyas una ruta de restauración insegura como
segura para producción. Consulta [verificación de la versión](../release-verification.md) (solo en inglés).
