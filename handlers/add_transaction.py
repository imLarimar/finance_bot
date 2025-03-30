from aiogram import Router, types
from aiogram.filters import Command

from database.crud import add_transaction
from core.logger import logger

add_transaction_router = Router()

@add_transaction_router.message(Command("add_transaction"))
async def add_transaction_func(message: types.Message):
    try:
        _, _, args = message.text.partition(" ")

        if not args:
            await message.reply("Ошибка! Используйте формат: /add_transaction <сумма> <категория>")
            return

        amount, category = args.split(" ", 1)
        user_id = message.from_user.id
        await add_transaction(user_id, int(amount), category)
        logger.info("Транзакция выполнена.")
    except ValueError:
        await message.reply("Ошибка! Сумма должна быть числом.")
    except Exception as err:
        logger.error(err)

