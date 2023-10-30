from typing import Optional, Dict

from fastapi import HTTPException


class AbstractAuthorizationException(HTTPException):
    status_code = 403
    detail = None

    def __init__(self, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail, headers=headers)


class TelegramAppHashNotValid(AbstractAuthorizationException):
    status_code = 403
    detail = "Telegram data not valid."


class TelegramUserNotFound(AbstractAuthorizationException):
    status_code = 404
    detail = "User with such data doesn`t exists."
