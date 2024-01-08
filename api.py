from fastapi import FastAPI
from src.routers.orderRouters import router as order_router
from src.routers.userRouters import router as user_router
from src.admin_way.starlette import admin

from fastapi import FastAPI

app = FastAPI()

app.title = 'Projeto App Care'

app.include_router(order_router)
app.include_router(user_router)
admin.mount_to(app)