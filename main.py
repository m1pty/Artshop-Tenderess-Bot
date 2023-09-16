import asyncio #ассинхронный запуск
import logging #настройки логгирования для запуска

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage #хранилища данных для состояний пользователей
from aiogram.enums.parse_mode import ParseMode #настройки разметки сообщений

import constConfig
from handlers import router

async def main():
    bot = Bot(token = constConfig.BOT_TOKEN, parse_mode = ParseMode.HTML)
    dp = Dispatcher(storage = MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot, allowed_updates = dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    asyncio.run(main())