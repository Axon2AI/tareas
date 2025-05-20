import os
from tinydb import TinyDB
from src.utils.config import get_config

class StorageService:
    """
    Servicio de almacenamiento basado en TinyDB.
    """
    def __init__(self):
        conf = get_config()
        db_path = conf.get('database', {}).get('path', 'tasks.json')
        self.db = TinyDB(db_path)

    def table(self, name: str):
        """
        Obtiene o crea una tabla en la base de datos.
        """
        return self.db.table(name)
