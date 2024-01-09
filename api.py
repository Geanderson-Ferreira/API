from fastapi import FastAPI
from src.admin_way.starlette import admin
from src.routers import routers

from fastapi import FastAPI

app = FastAPI()

app.title = 'Projeto App Care'

for router in routers: app.include_router(router)

admin.mount_to(app)