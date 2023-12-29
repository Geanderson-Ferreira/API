from DB_MANAGER.models import *
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from DB_MANAGER.config import DB
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from sqlalchemy.orm import joinedload

# Supondo que você tenha uma sessão do SQLAlchemy chamada 'session'
# e o modelo Base já esteja declarado


engine = create_engine(DB)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# Consulta para recuperar todos os registros da tabela 'orders' com todas as informações relacionadas


result = (
    session.query(Orders, Locations.LocationName, User.Username)
    .join(Locations)
    .join(OrderTypes)
    .join(User)
    .join(OrderStatus)
    .options(
        joinedload(Orders.location),
        joinedload(Orders.order_type),
        joinedload(Orders.created_by),
        joinedload(Orders.status)
    )
    .all()
)
serialized_result = list()


for order, local, nome in result:

    serialized_order = {
        'IdOrder': order.IdOrder,
        'Description': order.Description,
        'Status': order.Status,
        'CreatedBy': nome,
        'Location': local
    }

    serialized_result.append(serialized_order)


print(serialized_result)
