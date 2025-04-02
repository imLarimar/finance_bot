import asyncio

from aiogram import Bot, Dispatcher

from core.logger import logger
from core.config import BOT_TOKEN
from database.db import init_db, close_db
from handlers import all_routers

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    
    for router in all_routers:
        dp.include_router(router)
    
    try:
        await init_db()
        logger.info("Бот запущен.")
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(e)
    finally:
        await close_db()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем.")
    except Exception as err:
        logger.exception("Ошибка на самом верхнем уровне")