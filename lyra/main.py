#!/usr/bin/env python3
"""
Módulo principal para iniciar la aplicación Lyra.
"""
import sys

from src.gui.app import main as gui_main


def main():
    """Lanza la interfaz de usuario para gestión de tareas."""
    gui_main()


if __name__ == "__main__":
    sys.exit(main())