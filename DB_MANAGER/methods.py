from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from DB_MANAGER.models import Orders, Locations
from DB_MANAGER.config import DB
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.state import InstanceState


def alchemyencoder(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                # this will fail on non-encodable values, like other classes
                json.dumps(data)
                fields[field] = data
            except TypeError:
                # reverting to a representation
                fields[field] = str(data)
        # a json-encodable dict
        return fields

    if isinstance(obj, InstanceState):
        # an SQLAlchemy InstanceState
        return None

def queryOrders(id=None,location=None,creation_date=None,end_date=None,order_type=None,created_by=None,status=None):

    engine = create_engine(DB, echo=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(Orders)

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

    list_of_orders = list()

    for instance in query:
        list_of_orders.append(instance)
    
    list_of_json = [record.__dict__ for record in list_of_orders]
    return json.dumps(list_of_json, default=alchemyencoder)

def queryLocations(location_type=None, floor=None, hotel_id=None, location_id=None):

    engine = create_engine(DB, echo=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(Locations)

    if location_type is not None:
        query = query.filter(Locations.LocationType==location_type)
    if floor is not None:
        query = query.filter(Locations.Floor==floor)
    if hotel_id is not None:
        query = query.filter(Locations.Hotel==floor)
    if location_id is not None:
        query = query.filter(Locations.IDLocation==location_id)

    list_of_orders = list()

    for instance in query:
        list_of_orders.append(instance)
    
    list_of_json = [record.__dict__ for record in list_of_orders]
    return json.dumps(list_of_json, default=alchemyencoder)



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
