
from config_data.config import DataBaseConfig

class db:
    def __init__(self, db_config: DataBaseConfig):
        self.db_config = db_config
    
    def connect(self):
        self