from aiogram import Router, types, F
from aiogram.filters import CommandStart, ExceptionTypeFilter
from aiogram.types import ErrorEvent, Message

from core.config import WEB_APPLICATION_URL
from services.telegram.auth.exceptions import MessageDoesNotExist, SessionDoesNotExist

router = Router(name="authorization")


@router.error(ExceptionTypeFilter(MessageDoesNotExist, SessionDoesNotExist), F.update.message.as_("message"))
async def handle_authorization_exception(event: ErrorEvent, message: Message):
    await message.answer(f"{event.exception.message}, our team is already working on fixing it.")


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    web = types.WebAppInfo(url=WEB_APPLICATION_URL)
    button = types.InlineKeyboardButton(text="Open Cryptosales", web_app=web)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[button]])

    await message.answer("Crypto sales bot :3", reply_markup=keyboard)
