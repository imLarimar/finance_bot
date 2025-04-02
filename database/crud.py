from typing import Optional
from datetime import date

from sqlalchemy import exists, select

from .models import User, Transaction
from .db import async_session


async def exists_user(user_id: int) -> bool:
    async with async_session() as session:
        result = await session.execute(select(exists().where(User.user_id == user_id)))
        return result.scalar_one_or_none()

async def add_user(user_id: int):
    async with async_session() as session:
        user = User(user_id=user_id)
        session.add(user)
        await session.commit()

async def add_transaction(user_id: int, amount: int, category: str, date:Optional[date] = None):
    async with async_session() as session:
        transaction = Transaction(
            user_id = user_id,
            amount = amount,
            category = category,
            date = date
        )
        session.add(transaction)
        await session.commit()