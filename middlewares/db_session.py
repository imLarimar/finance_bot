from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import async_session

class DBSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        async with async_session() as session:
            data["db_session"] = session
            result = await handler(event, data)
            await session.commit()
            return result