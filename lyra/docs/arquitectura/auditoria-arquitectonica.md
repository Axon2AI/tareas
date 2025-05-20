# Auditoría Arquitectónica y de Código para LYRA

## 1. Estructura de Directorios

```text
/lyra/
├─ setup.py, pyproject.toml         # Empaquetado (setuptools)
├─ README.md                       # Visión general y quickstart
├─ requirements.txt                # Dependencias PyPI
├─ .gitignore
├─ Dockerfile                      # Imagen de escritorio (Python + GUI)
├─ scripts/package.sh              # Empaquetado PyInstaller
├─ ci/github-actions.yml           # CI: lint, test, build, package
├─ docs/
│  ├─ arquitectura/                # ADRs, decisiones de diseño
│  ├─ api/                         # Especificaciones de servicios
│  └─ uso/                         # Quickstart, guía de instalación
├─ src/
│  ├─ main.py                      # Punto de entrada
│  ├─ gui/                         # app, views, controllers
│  ├─ orchestrator/                # router, scheduler, intent_handlers
│  ├─ email_engine/                # IMAP, SMTP, OAuth, engine
│  ├─ task_mgr/                    # manager, repository, models
│  ├─ services/                    # NLU, voz, storage
│  ├─ models/                      # email, task
│  └─ utils/                       # config, logger
└─ tests/
   ├─ unitarios/                   # test_email_engine, test_task_mgr, test_nlu_service
   └─ e2e/scenarios/               # test_capture_task_via_voice
```

## 2. Inventario de Módulos y Paquetes

- **Entry points**: `main.py`, `scripts/package.sh`
- **Dependencias externas críticas**:
  - GUI: tkinter o PySide6
  - Email: imaplib, smtplib, google-api-python-client
  - Tasks: sqlite3 o tinydb
  - Scheduling: APScheduler
  - AI/NLU: openai, langchain, whisper
  - Voz: pyttsx3
  - Seguridad: cryptography (AES256)
  - Empaquetado: pyinstaller
- **Dependencias internas**: Orquestador, EmailEngine, TaskManager, NLUService

## 3. Configuración de Infraestructura y CI/CD

- **CI** (GitHub Actions): checkout, setup-python, install-deps, lint (black/flake8), pytest, build Docker, package PyInstaller, upload artifact
- **Despliegue local**: Dockerfile con Python:3.x, instala dependencias, copia código, ejecuta GUI de escritorio
- **Futura**: Kubernetes headless + PV; Terraform bucket S3 para logs

## 4. Revisión de la Capa de Datos

- **Modelos/Esquemas**: SQLite (Task, Email), TinyDB JSON
- **Migraciones**: Alembic o scripts SQL versionados en `/migrations`
- **Flujos E/S**: EmailEngine.fetch() → Email model → Repository.save_email(); TaskManager.create_task() → Repository.save_task(); Scheduler persiste jobs en DB

## 5. Revisión de la Lógica de Negocio

- **Servicios**: IntentHandlers, EmailEngine, TaskManager, NLUService
- **Orquestación**:
  1. GUI → Orquestador.router.detect_intent()
  2. Handler procesa e invoca EmailEngine/TaskManager
  3. Scheduler programa recordatorios/callbacks GUI

## 6. Revisión de la Capa de Presentación / API

- **GUI**: eventos de botones, props/inputs, callbacks → controller → orquestador
- **API interna**:
  - `EmailService.send_draft(prompt: str) -> JSON{to,subject,body}`
  - `TaskService.create_task(data: TaskCreateDTO) -> TaskDTO`

## 7. Diagramas de Alto Nivel (ASCII)

```
[GUI] <--> [Orquestador] <--> {EmailEngine, TaskManager, NLUService, Scheduler}

[Desktop App contenedor Docker]
- GPU/CPU-bound (NLU local)
- FS local (DB cifrada)

Flujo datos (capturar tarea):
GUI (voz) → VoiceService → NLUService → IntentHandler → TaskManager → DB
```

## 8. Flujos de Ejecución Críticos

### Escenario A: Captura por voz
1. GUI.voice_input()
2. voice_service.transcribe() → texto
3. nlu_service.parse(texto) → intent `crear_tarea` + params
4. router.dispatch(intent) → TaskHandler.create(params)
5. repository.save_task() → scheduler.schedule_reminder()
6. GUI.confirmación

### Escenario B: Triaging de correos
1. Scheduler diario dispara intent `triage_email`
2. EmailEngine.fetch_unread() → lista de Email
3. nlu_service.summarize_threads() → summaries
4. Handler convierte adjuntos-fechas en tareas via TaskManager
5. GUI.actualiza bandeja + Kanban

## 9. Documentación “Docs as Code”

Se versionan en `/docs/arquitectura`, `/docs/api`, `/docs/uso`:
- ADRs y decisiones (ej. `adr-0001-gui-toolkit.md`)
- Especificaciones (email_service.md, task_service.md, nlu_service.md)
- Guías de uso (quickstart.md, configuracion.md)

## 10. Ejemplos Prácticos

```python
from services.nlu_service import NLUService
from task_mgr.manager import TaskManager

nlu = NLUService()
intent, params = nlu.parse("prepara propuesta jueves")
TaskManager().create_task(**params)

from email_engine.engine import EmailEngine
draft = EmailEngine().generate_draft(to="rrhh@empresa.com", subject="Gracias entrevista")
EmailEngine().send(draft)
```

## 11. Convenciones y Estándares

- **PEP8**: snake_case, PascalCase
- **black/flake8** para lint y formateo
- **Commits**: `feat:`, `fix:`, `docs:`
- Plantillas en `/templates` para handlers, modelos, tests

# Observaciones finales

La propuesta actual forma un MVP sólido. Se recomienda MVP con Tkinter + SQLite + OpenAI function calling, luego iterar con OAuth y plugins de voz.