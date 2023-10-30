import json
from datetime import timedelta

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import TELEGRAM_TOKEN, JWT_ACCESS_TOKEN_EXPIRES_MINUTES
from core.database import get_session
from cryptosales.user import services as user_service
from cryptosales.user.exceptions import TelegramAppHashNotValid
from cryptosales.user.models import User
from cryptosales.user.schemas import JWTResponse, TelegramUserAuthorizationData
from cryptosales.user.security import access_token_security
from cryptosales.user.utils import validate_telegram_app_data, parse_telegram_app_init_data


async def validate_telegram_app_json_data(auth: TelegramUserAuthorizationData) -> dict:
    parsed_data = parse_telegram_app_init_data(auth.data)

    if "hash" not in parsed_data or not validate_telegram_app_data(auth.data, TELEGRAM_TOKEN):
        raise TelegramAppHashNotValid()

    return json.loads(parsed_data["user"])


async def is_user_already_exists(
    user_data: dict = Depends(validate_telegram_app_json_data),
    session: AsyncSession = Depends(get_session),
) -> bool:
    user = await user_service.get_user_by_telegram_id(session, user_data["id"])
    return True if user else False


async def get_or_create_user_with_telegram_user_data(
    user_data: dict = Depends(validate_telegram_app_json_data),
    session: AsyncSession = Depends(get_session),
) -> User:
    user = await user_service.get_or_create_user_by_telegram_id(session, user_data["id"])
    return user


async def create_jwt_using_telegram_data(
    is_user_exists: bool = Depends(is_user_already_exists),
    user: User = Depends(get_or_create_user_with_telegram_user_data),
) -> JWTResponse:
    subject = {"user": str(user.id), "is_user_new": not is_user_exists}
    expire = timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRES_MINUTES)
    return JWTResponse(access_token=access_token_security.create_access_token(subject, expire))
