from datetime import datetime

from src.task_mgr.models import TaskCreateDTO, TaskDTO
from src.services.storage_service import StorageService


class TaskRepository:
    """
    Repositorio para operaciones CRUD de tareas usando TinyDB.
    """
    def __init__(self):
        storage = StorageService()
        self.table = storage.table('tasks')

    def add(self, task: TaskCreateDTO) -> TaskDTO:
        """
        Inserta una nueva tarea y retorna su representación.
        """
        record = {
            'title': task.title,
            'description': task.description,
            'created_at': datetime.utcnow().isoformat()
        }
        doc_id = self.table.insert(record)
        return TaskDTO(id=doc_id, **record)

    def list(self) -> list[TaskDTO]:
        """
        Obtiene todas las tareas almacenadas.
        """
        tasks: list[TaskDTO] = []
        for doc in self.table.all():
            tasks.append(TaskDTO(
                id=doc.doc_id,
                title=doc.get('title', ''),
                description=doc.get('description', ''),
                created_at=doc.get('created_at', '')
            ))
        return tasks
