from sqlalchemy.orm import joinedload, Session
from sqlalchemy import func
from src.db_manager.models import Orders, Locations, OrderStatus, OrderTypes, User
from src.schemas.oder import OrderSchema, FilterOrderSchema
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status
from datetime import datetime

class OrderMethods:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def insert_order(self, order: OrderSchema):
        order_to_insert = Orders(
            Location=order.location,
            CreationDate=datetime.utcnow(),
            OrderType=order.order_type,
            ImageData=bytes(order.image_data, 'utf-8'),
            Description=order.description,
            CreatedBy=order.created_by,
            Status=order.status,
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