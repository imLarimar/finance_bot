from aiogram import Router, types
from aiogram.filters import CommandStart

from database.crud import add_user
from core.logger import logger

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message=types.Message):
    try:
        user_id = message.from_user.id
        await add_user(user_id)
        logger.info("Новый юзер внесен в таблицу.")
    except Exception as err:
        logger.error(err)


    
