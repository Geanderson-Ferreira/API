from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from models import Orders, Locations, User, Hotels, OrderTypes, OrderStatus
from config import DB

def create_user_example():

    #Base = declarative_base()
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
    hotel1 = Hotels(
        HotelName = 'Ibis Carlos Barbosa'
    )

    hotel2 = Hotels(
        HotelName = 'Ibis Porto Alegre Aeroporto'
    )


    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([hotel1, hotel2])
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

def insert_default_values_in_locations():

        local1 = Locations(
             LocationType = 'Quarto',
             LocationName = '752',
             Floor = 7,
             HotelId = 2
        )

        local2 = Locations(
             LocationType = 'Quarto',
             LocationName = '252',
             Floor = 7,
             HotelId = 1
        )
        local3 = Locations(
             LocationType = 'Area Social',
             LocationName = 'Banheiro Masculino Social',
             Floor = 0,
             HotelId = 2
        )

        local4 = Locations(
             LocationType = 'Quarto',
             LocationName = '259',
             Floor = 2,
             HotelId = 2
        )

        local5 = Locations(
             LocationType = 'Quarto',
             LocationName = '666',
             Floor = 6,
             HotelId = 1
        )
        local6 = Locations(
             LocationType = 'Area Social',
             LocationName = 'Banheiro Feminino Social',
             Floor = 0,
             HotelId = 2
        )



        engine = create_engine(DB)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add_all([local1, local2, local3, local4, local5, local6])
        session.commit()
        session.close()


from datetime import datetime
from datetime import datetime
import base64

def insert_order_with_image(location_id, order_type_id, description, created_by_id, status_id, image_path):
    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Lê os dados binários da imagem
    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read())

    order = Orders(
        Location=location_id,
        CreationDate=datetime.utcnow(),
        OrderType=order_type_id,
        Description=description,
        CreatedBy=created_by_id,
        Status=status_id,
        ImageData=image_data
    )

    session.add(order)
    session.commit()
    session.close()

def get_order_by_id(order_id):
    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use o método query para obter a ordem pelo IdOrder
    order = session.query(Orders).filter_by(IdOrder=order_id).first()

    # Certifique-se de verificar se a ordem foi encontrada
    if order:
        # Converte os dados binários da imagem de volta para bytes
        image_data = base64.b64decode(order.ImageData) if order.ImageData else None

        # Retorna um dicionário com os detalhes da ordem
        order_details = {
            'IdOrder': order.IdOrder,
            'Location': order.Location,
            'CreationDate': order.CreationDate,
            'EndDate': order.EndDate,
            'OrderType': order.OrderType,
            'Description': order.Description,
            'CreatedBy': order.CreatedBy,
            'Status': order.Status,
            'ImageData': image_data  # Dados binários da imagem
        }

        session.close()
        return order_details
    else:
        session.close()
        return None

# Exemplo de chamada da função
# Substitua '1' pelo IdOrder da ordem que deseja obter

"""

order_id_to_get = 1
order_details = get_order_by_id(order_id_to_get)

# Exibe os detalhes da ordem, se encontrada
if order_details:
    print(order_details)
else:
    print(f"A ordem com IdOrder {order_id_to_get} não foi encontrada.")

"""