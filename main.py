import asyncio

from aiogram import Bot, Dispatcher

from core.logger import logger
from core.config import BOT_TOKEN

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    
    try:
        logger.info("Бот запущен.")
        await dp.start_polling(bot)
    except Exception() as err:
        logger.info(err)
        
if __name__ == "__main__":
    asyncio.run(main())