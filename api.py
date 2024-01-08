from fastapi import FastAPI
from src.routers.orderRouters import router as order_router
from src.routers.userRouters import router as user_router
from src.routers.adminRouters import router as admin_router

from src.admin_way.starlette import admin
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.title = 'Projeto App Care'

app.include_router(order_router)
app.include_router(user_router)
app.include_router(admin_router)
#admin.mount_to(app)