from aiogram import Router, types
from aiogram.filters import CommandStart

from database.crud import exists_user, add_user
from core.logger import logger

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id

    try:
        is_existing = await exists_user(user_id)
        if not is_existing:
            await add_user(user_id)
            logger.info(f"Новый юзер {user_id} внесен в таблицу.")
    except Exception as e:
        logger.exception("Ошибка при проверке или добавлении пользователя")
        await message.answer("Что-то пошло не так. Попробуй позже.")
        return

    if is_existing:
        await message.reply("С возвращением! Будем и дальше считать твои деньги :))")
    else:
        await message.reply("Привет! Давай приступим ")
