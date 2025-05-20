import tkinter as tk
from typing import List

from src.task_mgr.models import TaskDTO


class MainView(tk.Tk):
    """
    Vista principal para gestión de tareas.
    """
    def __init__(self):
        super().__init__()
        self.title("Gestión de Tareas - Lyra MVP")
        self.geometry("400x500")
        self._controller = None
        self._setup_widgets()

    def _setup_widgets(self):
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        lbl_title = tk.Label(frame, text="Título de la tarea:")
        lbl_title.pack(anchor='w')
        self.entry_title = tk.Entry(frame)
        self.entry_title.pack(fill=tk.X)

        lbl_desc = tk.Label(frame, text="Descripción:")
        lbl_desc.pack(anchor='w', pady=(10, 0))
        self.entry_description = tk.Entry(frame)
        self.entry_description.pack(fill=tk.X)

        self.btn_add = tk.Button(frame, text="Agregar tarea", command=self._on_add_clicked)
        self.btn_add.pack(pady=10)

        lbl_tasks = tk.Label(frame, text="Tareas:")
        lbl_tasks.pack(anchor='w')
        self.listbox_tasks = tk.Listbox(frame)
        self.listbox_tasks.pack(fill=tk.BOTH, expand=True)

    def set_controller(self, controller):
        self._controller = controller
        self.refresh_tasks(self._controller.get_tasks())

    def _on_add_clicked(self):
        if self._controller:
            title = self.entry_title.get().strip()
            desc = self.entry_description.get().strip()
            if title:
                self._controller.add_task(title, desc)
                self.entry_title.delete(0, tk.END)
                self.entry_description.delete(0, tk.END)

    def refresh_tasks(self, tasks: List[TaskDTO]):
        self.listbox_tasks.delete(0, tk.END)
        for task in tasks:
            display = f"{task.id}: {task.title} ({task.created_at})"
            self.listbox_tasks.insert(tk.END, display)
