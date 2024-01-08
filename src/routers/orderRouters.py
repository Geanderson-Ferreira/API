from fastapi import APIRouter, Depends, status
from src.schemas.order import OrderSchema, FilterOrderSchema
from sqlalchemy.orm import Session
from src.db_manager.depends import get_db_session
from src.db_manager.methods.order_methods import OrderMethods
from fastapi.responses import JSONResponse
from src.db_manager.config import API_PREFIX
from src.db_manager.depends import token_verifier

router = APIRouter(prefix=API_PREFIX, dependencies=[Depends(token_verifier)])

@router.get('/list-orders/')
def list_orders(orderfilter: FilterOrderSchema = Depends(FilterOrderSchema), db_session: Session = Depends(get_db_session)):
    orderCase = OrderMethods(db_session)
    return orderCase.queryOrders(orderfilter)

@router.post('/insert-new-order/')
def insert_order(order: OrderSchema, db_session: Session = Depends(get_db_session)):

    orderCase = OrderMethods(db_session)
    orderCase.insertOrder(order)
    
    return JSONResponse(
        content={'msg':'success'},
        status_code=status.HTTP_201_CREATED
    )

@router.get('/orders_types_summarizeds/')
def orders_types_summarizeds(db_session: Session = Depends(get_db_session)):

    orderCase = OrderMethods(db_session)
    return orderCase.queryOrdersSummarized()

