from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.schemas.order import OrderSchema, FilterOrderSchema
from sqlalchemy.orm import Session
from src.db_manager.depends import get_db_session, token_verifier
from src.db_manager.methods.user_methods import UserMethod, UserSchemaForLogin

router = APIRouter(prefix="/admin", dependencies=[Depends(token_verifier)])
user_methods = UserMethod(db_session=None)  # Substitua por uma instância real de UserMethod com a sessão do banco de dados
templates = Jinja2Templates(directory="templates")  # Diretório onde os templates HTML estão localizados

@router.get('/login_admin', response_class=HTMLResponse)
async def login_admin(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post('/login_admin', response_class=HTMLResponse)
async def do_login_admin(request: Request, user_login: UserSchemaForLogin, db_session: Session = Depends(get_db_session)):
    try:
        # Autenticação usando o método user_login do UserMethod
        token_data = user_methods.user_login(user_login=user_login)

        # Redirecionar para a rota protegida com o token
        return RedirectResponse(url=f"{API_PREFIX}/admin/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    except HTTPException as e:
        # Tratar erros de autenticação
        return templates.TemplateResponse("login.html", {"request": request, "error_message": e.detail})

@router.get('/dashboard', response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
