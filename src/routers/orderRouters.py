from fastapi import Query, APIRouter
from typing import Optional
from src.db_manager.methods.order_methods import queryOrders, queryOrdersSummarized, insertNewOrder

orders_router = APIRouter(prefix='/api')

@orders_router.get('/list-orders/')
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

@orders_router.post('/insert-new-order/')
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

@orders_router.get('/orders_types_summarizeds/')
def orders_types_summarizeds():
    return queryOrdersSummarized()
