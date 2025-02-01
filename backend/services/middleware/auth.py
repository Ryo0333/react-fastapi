from typing import Awaitable, Callable

from fastapi import Request
from jose import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from core.config import settings


class JwtAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if not request.url.path.startswith("/admin"):
            return await call_next(request)
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return Response(content="Unauthorized", status_code=401)
        if not auth_header.startswith("Bearer "):
            return Response(content="Invalid token", status_code=401)
        token = auth_header.split(" ")[1]  # "Bearer {token}" の形式なので分割

        try:
            # JWT をデコードしてユーザー情報を取得
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            role = payload.get("role")

            if role != "admin":
                return Response(content="Forbidden", status_code=403)

        except jwt.ExpiredSignatureError:
            return Response(content="Token expired", status_code=401)
        except jwt.InvalidTokenError:
            return Response(content="Invalid token", status_code=401)

        return await call_next(request)
