import logging


from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

class userRouter:
    def __init__(self):
        self.router = Router()
        self._register_handlers()
    
    def _register_handlers(self):
        self.router.message.register(self.startCommand, CommandStart())
    
    async def startCommand(self, message: Message):
        await message.answer(text="hello")

