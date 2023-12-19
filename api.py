from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from DB_MANAGER.methods import get_orders_as_json

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

@app.get('/list-orders-demo')
def stated():
    return {
  "orders": [
    {
      "IdOrder": 1,
      "Location": 101,
      "CreationDate": "2023-01-15T10:30:00",
      "EndDate": "2023-01-20T15:45:00",
      "OrderType": 1,
      "Description": "Manutenção na TV",
      "CreatedBy": 201,
      "Status": "Pending",
      "ImageData": 'null'
    },
    {
      "IdOrder": 2,
      "Location": 102,
      "CreationDate": "2023-01-18T12:15:00",
      "EndDate": 'null',
      "OrderType": 2,
      "Description": "Conserto do Ar Condicionado",
      "CreatedBy": 202,
      "Status": "In Progress",
      "ImageData": 'null'
    },
    {
      "IdOrder": 3,
      "Location": 103,
      "CreationDate": "2023-01-20T14:00:00",
      "EndDate": "2023-01-22T16:30:00",
      "OrderType": 3,
      "Description": "Troca de Lâmpadas",
      "CreatedBy": 203,
      "Status": "Completed",
      "ImageData": 'null'
    }
  ]
}


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
    return get_orders_as_json(order)


@app.get('/api/get-order/')
def get_order():
    return{'funcao': 'get-order'}

@app.get('/api/list-rooms/')
def list_rooms():
    return {'funcao': 'list-rooms'}

@app.get('/api/get-orders-type-summarized')
def get_orders_type_summarized():
    return {'funcao': 'get-orders-type-summarized'}



