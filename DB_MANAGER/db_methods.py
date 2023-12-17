from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from models import User, Hotels, OrderTypes, OrderStatus
from config import DB

def create_user_example():

    Base = declarative_base()
    engine = create_engine(DB)

    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(
        Username='usuario1',
        Password='senha1',
        FullName='Usuário 1',
        Email='usuario1@example.com'
    )
    user2 = User(
        Username='usuario2',
        Password='senha2',
        FullName='Usuário 2',
        Email='usuario2@example.com'
    )
    session.add_all([user1, user2])
    session.commit()
    session.close()


def create_hotel_example():
    icb = Hotels(
        HotelName = 'Ibis Carlos Barbosa'
    )

    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(icb)
    session.commit()
    session.close()
    
def insert_default_values_in_order_types():

    defaul_types = ['Pintura', 'Mobília', 'TV', 'Telefone', 'Frigobar', 'Ar Condicionado', 'Iluminação', 'Banheiro' ,'Outros']

    for type in defaul_types:

        type = OrderTypes(
            OrderTypeName = type
        )

        engine = create_engine(DB)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(type)
        session.commit()
        session.close()

def insert_default_values_in_order_status():

    defaul_types = ['Sent to Block', 'Pendente', 'Encerrada']

    for type in defaul_types:

        type = OrderStatus(
            StatusName = type
        )

        engine = create_engine(DB)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(type)
        session.commit()
        session.close()

insert_default_values_in_order_status()