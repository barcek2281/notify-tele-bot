import psycopg2

from config_data.config import DataBaseConfig

class Database:
    def __init__(self, db_config: DataBaseConfig):
        self.db_config = db_config
        self.connection = psycopg2.connect(database=db_config.DB, 
                                        user=db_config.User, 
                                        password=db_config.Password, 
                                        host="localhost",
                                        port=db_config.Port)
        self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE users(user_id INTEGER)")