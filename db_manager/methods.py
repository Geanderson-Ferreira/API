from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine, func
from db_manager.models import Orders, Locations, OrderStatus, OrderTypes, User
from db_manager.config import DB
from datetime import datetime
from sqlalchemy.orm import Session
from db_manager.base import Base

def queryOrders(id=None,location=None,creation_date=None,end_date=None,order_type=None,created_by=None,status=None):

    #Gera conexao banco
    engine = create_engine(DB)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    
    #Query inicial com os joins as outras tabelas
    query = (
        session.query(Orders, Locations.LocationName, User.Username, OrderStatus.StatusName, OrderTypes.OrderTypeName)
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
    if id is not None:
        query = query.filter(Orders.IdOrder==id)

    if location is not None:
        query = query.filter(Orders.Location==location)
    
    if creation_date is not None:
        query = query.filter(Orders.CreationDate==creation_date)
    
    if end_date is not None:
        query = query.filter(Orders.EndDate==end_date)
    
    if order_type is not None:
        query = query.filter(Orders.OrderType==order_type)
    
    if created_by is not None:
        query = query.filter(Orders.CreatedBy==created_by)
    
    if status is not None:
        query = query.filter(Orders.Status==status)
    
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


def queryOrdersSummarized():

    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    order_counts = (
        session.query(OrderTypes.OrderTypeName, func.count(Orders.IdOrder))
            .join(Orders, OrderTypes.IDTypeOrder == Orders.OrderType)
            .filter(Orders.Status == 2)
            .group_by(OrderTypes.OrderTypeName)
                .all()
    )

    # Criando um dicionário para armazenar os resultados
    return {"order_counts": [{"OrderTypeName": order_type, "Count": count} for order_type, count in order_counts]}

def insertNewOrder(location=None, description=None, order_type=None,created_by=None,status=None, hotel_id=None):

    engine = create_engine(DB, echo=False)
    Base.metadata.create_all(engine)
    session = Session(engine)

    data_to_insert = {"Location": location, "CreationDate": datetime.utcnow(), "EndDate": None, "OrderType": order_type,
        "ImageData": b"sample_image_data", "Description": description, "CreatedBy": created_by, "Status": status, "HotelId": hotel_id}
    
    session.add(Orders(**data_to_insert))
    session.commit()
    session.close()

    return data_to_insert