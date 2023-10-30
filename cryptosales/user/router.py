from fastapi import APIRouter, Depends

from cryptosales.user.dependencies import create_jwt_using_telegram_data
from cryptosales.user.schemas import JWTResponse

router = APIRouter()


@router.post("/telegram/login")
async def authorize_user_with_telegram(jwt_token: JWTResponse = Depends(create_jwt_using_telegram_data)) -> JWTResponse:
    return jwt_token
