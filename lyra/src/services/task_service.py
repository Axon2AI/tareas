from src.task_mgr.models import TaskCreateDTO, TaskDTO
from src.task_mgr.repository import TaskRepository
from src.task_mgr.manager import TaskManager


class TaskService:
    """
    Servicio de gestión de tareas.
    """
    def __init__(self):
        self.repository = TaskRepository()
        self.manager = TaskManager(self.repository)

    def create_task(self, data: TaskCreateDTO) -> TaskDTO:
        """
        Crea una tarea a partir de un DTO de creación.
        """
        return self.manager.create_task(data.title, data.description)

    def list_tasks(self) -> list[TaskDTO]:
        """
        Obtiene todas las tareas.
        """
        return self.manager.list_tasks()