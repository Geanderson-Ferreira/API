from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime
from DB_MANAGER.models import *
from DB_MANAGER.config import DB

#Funcao que popula o Banco
def populate():
    Base = declarative_base()
    engine = create_engine(DB, echo=False)
    Base.metadata.create_all(engine)
    session = Session(engine)

#Dados Aleatorios para preenchimento
    hotel_data = [
        {"HotelName": "Hotel A"},
        {"HotelName": "Hotel B"},
        {"HotelName": "Hotel C"},
        {"HotelName": "Hotel D"},
        {"HotelName": "Hotel E"},
        {"HotelName": "Hotel F"},
        {"HotelName": "Hotel G"},
    ]

    location_data = [
        {"LocationType": "Quarto", "LocationName": "752", "Floor": 7, "HotelId": 1},
        {"LocationType": "Quarto", "LocationName": "369", "Floor": 3, "HotelId": 1},
        {"LocationType": "Quarto", "LocationName": "254", "Floor": 2, "HotelId": 1},
        {"LocationType": "Eventos", "LocationName": "Sala de Eventos A", "Floor": 2, "HotelId": 2},
        {"LocationType": "BackOffice", "LocationName": "Escritorio", "Floor": 0, "HotelId": 2},
        {"LocationType": "FrontOffice", "LocationName": "Recepcao", "Floor": 0, "HotelId": 3},
        {"LocationType": "FrontOffice", "LocationName": "Lobby", "Floor": 0, "HotelId": 1},
    ]

    order_data = [
        {"Location": 1, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 1,
        "ImageData": b"sample_image_data", "Description": "Order 1", "CreatedBy": 1, "Status": 1, "HotelId": 1},
        {"Location": 2, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 2,
        "ImageData": b"sample_image_data", "Description": "Order 2", "CreatedBy": 2, "Status": 2, "HotelId": 2},
        {"Location": 3, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 3,
        "ImageData": b"sample_image_data", "Description": "Order 3", "CreatedBy": 3, "Status": 2, "HotelId": 3},
        {"Location": 4, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 4,
        "ImageData": b"sample_image_data", "Description": "Order 4", "CreatedBy": 2, "Status": 2, "HotelId": 4},
        {"Location": 5, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 5,
        "ImageData": b"sample_image_data", "Description": "Order 5", "CreatedBy": 1, "Status": 2, "HotelId": 5},
        {"Location": 6, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 6,
        "ImageData": b"sample_image_data", "Description": "Order 6", "CreatedBy": 3, "Status": 2, "HotelId": 6},
        {"Location": 7, "CreationDate": datetime.utcnow(), "EndDate": datetime.utcnow(), "OrderType": 6,
        "ImageData": b"sample_image_data", "Description": "Order 7", "CreatedBy": 2, "Status": 2, "HotelId": 7},  
    ]

    user_data = [
        {"Username": "user1", "Password": "password1", "FullName": "User One", "Email": "user1@example.com"},
        {"Username": "user2", "Password": "password2", "FullName": "User Two", "Email": "user2@example.com"},
        {"Username": "user3", "Password": "password3", "FullName": "User Three", "Email": "user3@example.com"},
        {"Username": "user4", "Password": "password4", "FullName": "User Four", "Email": "user4@example.com"},
        {"Username": "user5", "Password": "password5", "FullName": "User Five", "Email": "user5@example.com"},
        {"Username": "user6", "Password": "password6", "FullName": "User Six", "Email": "user6@example.com"},
    ]

    order_type_data = [
        {"OrderTypeName": "Pintura"},
        {"OrderTypeName": "Mobilia"},
        {"OrderTypeName": "TV"},
        {"OrderTypeName": "Telefone"},
        {"OrderTypeName": "Frigobar"},
        {"OrderTypeName": "Ar Condicionado"},
        {"OrderTypeName": "Iluminacao"},
        {"OrderTypeName": "Banheiro"},
        {"OrderTypeName": "Outros"},
    ]

    order_status_data = [
        {"StatusName": "Pendente"},
        {"StatusName": "A Bloquear"},
        {"StatusName": "Finalizado"},
    ]

#Insere os dados
    try:

        for hotel in hotel_data:
            session.add(Hotels(**hotel))

        for location in location_data:
            session.add(Locations(**location))

        for order in order_data:
            session.add(Orders(**order))

        for user in user_data:
            session.add(User(**user))

        for order_type in order_type_data:
            session.add(OrderTypes(**order_type))

        for order_status in order_status_data:
            session.add(OrderStatus(**order_status))

        session.commit()
        session.close()

        print('>> DB POPULADO')
    except Exception as erro:

        print('>> ERRO:\n\n', erro, '\n')
