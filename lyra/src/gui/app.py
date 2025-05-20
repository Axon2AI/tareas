from src.services.task_service import TaskService
from src.gui.views import MainView
from src.gui.controllers import MainController


def main():
    """
    Punto de entrada para la interfaz de gestión de tareas.
    """
    service = TaskService()
    view = MainView()
    MainController(view, service)
    view.mainloop()


if __name__ == "__main__":
    main()
