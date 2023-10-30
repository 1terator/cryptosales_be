from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class UserLocalizationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        language = request.headers.get("Accept-Language", None)
        if language:
            pass
        response = await call_next(request)
        return response
