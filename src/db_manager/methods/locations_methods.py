from sqlalchemy.orm import Session
from src.db_manager.models import Order
from src.schemas.order import OrderSchema
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status
from datetime import datetime

class OrderMethods:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def insert_order(self, order: OrderSchema):
        order_to_insert = Order(
            Location=order.location_id,
            CreationDate=datetime.utcnow(),
            OrderType=order.order_type_id,
            ImageData=bytes(order.image_data, 'utf-8'),
            Description=order.description,
            UserId=order.created_by_id,
            Status=order.status_id,
            HotelId=order.hotel_id
        )

        try:
            self.db_session.add(order_to_insert)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Erro de Integridade do Banco. Verifique os dados que esta tentando inserir.',
            )