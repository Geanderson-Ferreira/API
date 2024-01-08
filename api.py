from fastapi import FastAPI
from src.routers.orderRouters import router as order_router
from src.routers.userRouters import router as user_router
from src.admin_way.starlette import admin

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

app = FastAPI()


#@app.get("/", response_class=HTMLResponse)
#def read_root(request: Request):
#    return templates.TemplateResponse("login.html", {"request": request, "message": "Hello, FastAPI!"})

app.include_router(order_router)
app.include_router(user_router)
admin.mount_to(app)