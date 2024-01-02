from fastapi import Query, APIRouter, Depends, status
from typing import Optional
from src.db_manager.methods.order_methods import queryOrders
from src.schemas.oder import OrderSchema
from sqlalchemy.orm import Session
from src.db_manager.depends import get_db_session
from src.db_manager.methods.order_methods import OrderMethods
from fastapi.responses import JSONResponse
from src.db_manager.config import API_PREFIX

router = APIRouter(prefix=API_PREFIX)

@router.get('/list-orders/')
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

@router.post('/insert-new-order/')
def insert_order(order: OrderSchema, db_session: Session = Depends(get_db_session)):

    orderCase = OrderMethods(db_session)
    orderCase.insert_order(order)
    
    return JSONResponse(
        content={'msg':'success'},
        status_code=status.HTTP_201_CREATED
    )


@router.get('/orders_types_summarizeds/')
def orders_types_summarizeds(db_session: Session = Depends(get_db_session)):

    orderCase = OrderMethods(db_session)
    return orderCase.queryOrdersSummarized()

