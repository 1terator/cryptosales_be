from pydantic import BaseModel, Field


class TelegramUserAuthorizationData(BaseModel):
    data: str = Field(...)


class JWTResponse(BaseModel):
    access_token: str = Field(...)
