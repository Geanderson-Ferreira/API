from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    IdOrder: Optional[int]
    Location: Optional[int]
    CreationDate: Optional[str]
    EndDate: Optional[str]
    OrderType: Optional[int]
    ImageData: Optional[bytes]
    Description: Optional[str]
    CreatedBy: Optional[int]
    Status: Optional[str]

app = FastAPI()

@app.get('/')
def stated():
    return 'API ACESSADA'

@app.get('/api/list-orders/')
def list_orders(
    IdOrder: Optional[int] = Query(None, alias="IdOrder"),
    Location: Optional[int] = Query(None, alias="Location"),
    CreationDate: Optional[str] = Query(None, alias="CreationDate"),
    EndDate: Optional[str] = Query(None, alias="EndDate"),
    OrderType: Optional[int] = Query(None, alias="OrderType"),
    ImageData: Optional[bytes] = Query(None, alias="ImageData"),
    Description: Optional[str] = Query(None, alias="Description"),
    CreatedBy: Optional[int] = Query(None, alias="CreatedBy"),
    Status: Optional[str] = Query(None, alias="Status")
):
    order = Order(
        IdOrder=IdOrder,
        Location=Location,
        CreationDate=CreationDate,
        EndDate=EndDate,
        OrderType=OrderType,
        ImageData=ImageData,
        Description=Description,
        CreatedBy=CreatedBy,
        Status=Status
    )
    return order

@app.get('/api/get-order/')
def get_order():
    return{'funcao': 'get-order'}

@app.get('/api/list-rooms/')
def list_rooms():
    return {'funcao': 'list-rooms'}

@app.get('/api/get-orders-type-summarized')
def get_orders_type_summarized():
    return {'funcao': 'get-orders-type-summarized'}



