from fastapi_jwt import JwtAccessBearer

from core.config import JWT_SECRET_KEY, JWT_ALGORITHM

access_token_security = JwtAccessBearer(secret_key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM, auto_error=True)
