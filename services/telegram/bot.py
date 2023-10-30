from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from core.config import TELEGRAM_TOKEN
from core.database import session_pool
from services.telegram.auth.commands import router as auth_router
from services.telegram.auth.middlewares import UserAntiFloodMiddleware
from services.telegram.database.middlewares import DatabaseSessionMiddleware

bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher()

# include middlewares
dispatcher.message.middleware(DatabaseSessionMiddleware(session_pool))
dispatcher.message.middleware(UserAntiFloodMiddleware())

# include routers
dispatcher.include_router(auth_router)
