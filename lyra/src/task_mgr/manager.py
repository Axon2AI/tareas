from src.task_mgr.models import TaskCreateDTO, TaskDTO
from src.task_mgr.repository import TaskRepository


class TaskManager:
    """
    Lógica de negocio para la gestión de tareas.
    """
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str = "") -> TaskDTO:
        """
        Crea una nueva tarea con título y descripción.
        """
        dto = TaskCreateDTO(title=title, description=description)
        return self.repository.add(dto)

    def list_tasks(self) -> list[TaskDTO]:
        """
        Devuelve todas las tareas existentes.
        """
        return self.repository.list()
