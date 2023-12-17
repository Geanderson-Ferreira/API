from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def primeira_requisicao():
    return {'info': 'Hello World'}

@app.get('/segundo/')
def segunda_requisicao():
    return {'info': 'Segunda requisicao'}


uvicorn.run(app)

