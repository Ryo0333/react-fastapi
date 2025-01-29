from fastapi import APIRouter

from api.admin import admin_router
from api.sales import sales_router
from api.user import user_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(admin_router)
api_router.include_router(sales_router)
