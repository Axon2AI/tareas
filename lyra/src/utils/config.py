import os
from dotenv import load_dotenv
import yaml

load_dotenv()

def get_config() -> dict:
    """
    Carga la configuración desde un archivo YAML/JSON y variables de entorno.
    """
    config: dict = {}
    config_file = os.getenv('CONFIG_FILE', 'config.yaml')
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                cfg = yaml.safe_load(f)
                if isinstance(cfg, dict):
                    config = cfg
        except Exception:
            pass
    db_url = os.getenv('DATABASE_URL')
    if db_url:
        config.setdefault('database', {})['path'] = db_url
    return config
