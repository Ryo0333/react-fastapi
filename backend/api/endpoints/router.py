from fastapi import APIRouter

from api.endpoints.admin import admin_router
from api.endpoints.sales import sales_router
from api.endpoints.token import token_router
from api.endpoints.users import user_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(admin_router)
api_router.include_router(sales_router)
api_router.include_router(token_router)
