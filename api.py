from fastapi import FastAPI
from src.routers.order_routers import router as order_router
from src.routers.user_routers import router as user_router
from src.routers.location_routers import router as location_router
from src.admin_way.starlette import admin

from fastapi import FastAPI

app = FastAPI()

app.title = 'Projeto App Care'

app.include_router(user_router)
app.include_router(order_router)
app.include_router(location_router)
admin.mount_to(app)