from aiogram.types import Message
from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from datetime import datetime


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in ([i for i in (range(8, 19))])


class OfficeHorsMiddlewakre(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],

    ) -> Any:
        if office_hours():
            return await handler(event, data)
        await event.answer("Я Вас не звал идите на ....")
