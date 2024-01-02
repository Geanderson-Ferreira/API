from fastapi import FastAPI
from src.routers.orderRouters import orders_router

#Para rodar a API, esteja no mesmo diretorio desde arquivo e rodar:
#>> uvicorn api:app
#>> uvicorn api:app --host 10.0.0.102 --port 8000 --reload

app = FastAPI()

@app.get('/')
def check_health():
    return 'API rodando...'

app.include_router(orders_router)