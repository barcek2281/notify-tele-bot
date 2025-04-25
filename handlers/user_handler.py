import logging


from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config_data.config import DataBaseConfig
from db.postgres.postgre import Database

class UserRouter:
    def __init__(self, db_config: DataBaseConfig):
        self.router = Router()
        self.db = Database(db_config=db_config)
        self._register_handlers()
    
    def _register_handlers(self):
        self.router.message.register(self.startCommand, CommandStart())
    
    async def startCommand(self, message: Message):
        user_id = message.from_user.id
        self.db.cursor.execute(f"INSER INTO users(user_id) VALUES({user_id})")
        await message.answer(text=f"hello, {user_id}")

