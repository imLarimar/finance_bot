from typing import Optional
from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from .models import User, Transaction


async def add_transaction(user_id: int, amount: int, category: str, session: AsyncSession, date:Optional[date] = None):
        transaction = Transaction(
            user_id = user_id,
            amount = amount,
            category = category,
            date = date
        )
        session.add(transaction)