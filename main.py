import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import load_env, Config
from handlers import user_handler

logger = logging.getLogger(__name__)

async def main():
    config: Config = load_env()


    logging.basicConfig(
        level=config.log_config.Level,
        format=config.log_config.Format)

    logger.info('Starting bot')


    bot = Bot(
        token=config.tg_bot.BotToken,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    userRouter = user_handler.userRouter(db_config=config.db_config)

    dp = Dispatcher()
    dp.include_router(userRouter.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())