from sqlalchemy.orm import sessionmaker, joinedload, Session
from sqlalchemy import create_engine, func
from src.db_manager.models import Orders, Locations, OrderStatus, OrderTypes, User
from src.db_manager.config import DATABASE
from src.schemas.oder import OrderSchema, FilterOrderSchema
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status


class OrderMethods:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def insert_order(self, order: OrderSchema):
        order_to_insert = Orders(
            Location=order.location,
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
                detail='Order Data Already Exists'
            )
    
    def queryOrdersSummarized(self):

        #engine = create_engine(DATABASE)
        #Session = sessionmaker(bind=engine)
        #session = Session()

        order_counts = (
            self.db_session.query(OrderTypes.OrderTypeName, func.count(Orders.IdOrder))
                .join(Orders, OrderTypes.IDTypeOrder == Orders.OrderType)
                .filter(Orders.Status == 2)
                .group_by(OrderTypes.OrderTypeName)
                    .all()
        )

        # Criando um dicionário para armazenar os resultados
        return {"order_counts": [{"OrderTypeName": order_type, "Count": count} for order_type, count in order_counts]}

    def queryOrders(self, orderFilter: FilterOrderSchema):

        #Gera conexao banco
        #engine = create_engine(DATABASE)
        #Session = sessionmaker()
        #Session.configure(bind=engine)
        #session = Session()
        
        #Query inicial com os joins as outras tabelas
        query = (
            self.db_session.query(Orders, Locations.LocationName, User.Username, OrderStatus.StatusName, OrderTypes.OrderTypeName)
            .join(Locations, Orders.Location == Locations.IDLocation)
            .join(OrderTypes)
            .join(User)
            .join(OrderStatus)
            .options(
                joinedload(Orders.location),
                joinedload(Orders.order_type),
                joinedload(Orders.created_by),
                joinedload(Orders.status)
            )
        )

        #Aplica os filtros que o usuario colocou, caso colocou.
        if orderFilter.id is not None:
            query = query.filter(Orders.IdOrder==orderFilter.id)

        if orderFilter.location is not None:
            query = query.filter(Orders.Location==orderFilter.location)
        
        if orderFilter.order_type is not None:
            query = query.filter(Orders.OrderType==orderFilter.order_type)
        
        if orderFilter.created_by is not None:
            query = query.filter(Orders.CreatedBy==orderFilter.created_by)
        
        if orderFilter.status is not None:
            query = query.filter(Orders.Status==orderFilter.status)

        if orderFilter.hotel_id is not None:
            query = query.filter(Orders.HotelId==orderFilter.hotel_id)

        #Cria lista para serializar como JSON
        serialized_result = list()

        for order, local, nome, status, order_type in query:

            serialized_order = {
                'IdOrder': order.IdOrder,
                'Description': order.Description,
                'Status': status,
                'CreatedBy': nome,
                'Location': local,
                'Type': order_type
            }

            serialized_result.append(serialized_order)

        return serialized_result