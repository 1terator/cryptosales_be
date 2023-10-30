import asyncio
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class UserAntiFloodMiddleware(BaseMiddleware):
    async def __call__(
            self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]
    ) -> Any:
        await asyncio.sleep(1)
        return await handler(event, data)
