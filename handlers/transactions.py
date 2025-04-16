from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession


from database.crud import add_transaction
from core.logger import logger

add_transaction_router = Router()

@add_transaction_router.message(Command("add_transaction"))
async def add_transaction_func(message: types.Message, db_session: AsyncSession):
    _, _, args = message.text.partition(" ")

    if not args:
        await message.reply("Ошибка! Используйте формат: /add_transaction <сумма> <категория>")
        return

    try:
        amount_str, category = args.split(" ", 1)
        amount = float(amount_str.replace(",", "."))
    except ValueError:
        await message.reply("Ошибка! Сумма должна быть числом (например: 12.5 или 100).")
        return

    try:
        user_id = message.from_user.id
        await add_transaction(user_id, amount, category, db_session)
        logger.info(f"Транзакция: {user_id} | {amount} | {category}")
        await message.reply(f"Транзакция на {amount}₽ в категории '{category}' успешно добавлена!")
    except Exception as err:
        logger.exception("Ошибка при добавлении транзакции")
        await message.reply("Ошибка при добавлении транзакции. Попробуйте позже.")