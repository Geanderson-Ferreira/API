from fastapi import FastAPI, Query
from typing import Optional
from db_manager.methods import queryOrders, queryOrdersSummarized, insertNewOrder

#Para rodar a API, esteja no mesmo diretorio desde arquivo e rodar:
#>> uvicorn api:app
#>> uvicorn api:app --host 10.0.0.102 --port 8000 --reload

app = FastAPI()


@app.get('/api/list-orders/')
def list_orders(
    IdOrder: Optional[int] = Query(None, alias="IdOrder"),
    Location: Optional[int] = Query(None, alias="Location"),
    CreationDate: Optional[str] = Query(None, alias="CreationDate"),
    EndDate: Optional[str] = Query(None, alias="EndDate"),
    OrderType: Optional[int] = Query(None, alias="OrderType"),
    CreatedBy: Optional[int] = Query(None, alias="CreatedBy"),
    Status: Optional[str] = Query(None, alias="Status")
    ):
    
    return queryOrders(id=IdOrder, 
                       location=Location, 
                       creation_date=CreationDate,
                       end_date=EndDate,
                       order_type=OrderType,
                       created_by=CreatedBy,
                       status=Status)

@app.get('/api/orders_types_summarizeds/')
def orders_types_summarizeds():
    return queryOrdersSummarized()

@app.post('/api/insert-new-order/')
def insert_order(
    Location: int = Query(None, alias="Location"),
    Description: str = Query(None, alias="Description"),
    OrderType: int = Query(None, alias="OrderType"),
    CreatedBy: int = Query(None, alias="CreatedBy"),
    Status: str = Query(None, alias="Status")
    ):
    
    return insertNewOrder(
                       location=Location,
                       description=Description,
                       order_type=OrderType,
                       created_by=CreatedBy,
                       status=Status)
    