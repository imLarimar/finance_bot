from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User
from core.logger import logger


start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: types.Message, db_session: AsyncSession):
    user_id = message.from_user.id

    try:
        result = await db_session.execute(
            select(exists().where(User.user_id == user_id))
        )
        is_existing = result.scalar()

        if not is_existing:
            db_session.add(User(user_id=user_id))
            logger.info(f"Добавлен новый пользователь: {user_id}")
            await message.answer("Привет! Давай приступим")
        else:
            logger.info(f"Пользователь вернулся: {user_id}")
            await message.answer("С возвращением! Будем и дальше считать твои деньги :))")

    except Exception as e:
        logger.exception(f"Ошибка в start_handler для user_id={user_id}")
        await message.answer("Что-то пошло не так. Попробуй позже.")


