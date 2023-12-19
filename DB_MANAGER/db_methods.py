from models import Orders
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DB


def getOrder():
    """
    status
    OrderType
    RoomNumber
    """

    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        orders = session.query(Orders).all()
        print(orders[0].IdOrder)
