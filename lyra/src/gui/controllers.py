from src.task_mgr.models import TaskCreateDTO
from src.services.task_service import TaskService


class MainController:
    """
    Controlador que une la vista principal con la lógica de tareas.
    """
    def __init__(self, view, service: TaskService):
        self.view = view
        self.service = service
        self.view.set_controller(self)

    def add_task(self, title: str, description: str):
        """
        Crea una tarea y actualiza la vista.
        """
        dto = TaskCreateDTO(title=title, description=description)
        self.service.create_task(dto)
        self.view.refresh_tasks(self.get_tasks())

    def get_tasks(self):
        """
        Recupera la lista de tareas.
        """
        return self.service.list_tasks()
