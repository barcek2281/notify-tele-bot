import logging


from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()
logger = logging.getLogger(__name__)

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="hello")
