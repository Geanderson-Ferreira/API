from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine, select
from DB_MANAGER.models import Base, Orders, Locations, OrderStatus, OrderTypes, User
from DB_MANAGER.config import DB
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.state import InstanceState

def queryOrders(id=None,location=None,creation_date=None,end_date=None,order_type=None,created_by=None,status=None):

    engine = create_engine(DB)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    
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

def queryOrders2(id=None,location=None,creation_date=None,end_date=None,order_type=None,created_by=None,status=None):

    engine = create_engine(DB)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = (
        session.query(Orders, Locations.LocationName, User.Username, OrderStatus.StatusName)
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

    result = result.filter(Orders.IdOrder>2).all()

    serialized_result = list()

    for order, local, nome, status in result:

        serialized_order = {
            'IdOrder': order.IdOrder,
            'Description': order.Description,
            'Status': status,
            'CreatedBy': nome,
            'Location': local
        }

        serialized_result.append(serialized_order)

    return serialized_result


























def queryLocations(location_type=None, floor=None, hotel_id=None, location_id=None):

    return [{'valor' : 'funcao nao implementada ainda'}]

def queryOrdersSummarized():
    from sqlalchemy import func
    engine = create_engine(DB)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
# Supondo que você tenha uma sessão do SQLAlchemy chamada 'session'
    result = session.query(Orders.OrderType, func.count().label('total_orders'))
    result.group_by(Orders.OrderType).all()
    print(result)
    for row in result:
        order_type, total_orders = row
        print(f"Order Type {order_type}: {total_orders} orders")

