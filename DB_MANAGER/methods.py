from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Query
from DB_MANAGER.models import Orders
from DB_MANAGER.config import DB
import json

def get_orders_as_json(order_filter):
    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        # Constrói a consulta base
        query = session.query(Orders)

        # Adiciona condições de filtro se os parâmetros foram fornecidos
        if order_filter.IdOrder is not None:
            query = query.filter(Orders.IdOrder == order_filter.IdOrder)
        if order_filter.Location is not None:
            query = query.filter(Orders.Location == order_filter.Location)
        if order_filter.CreationDate is not None:
            query = query.filter(Orders.CreationDate == order_filter.CreationDate)
        # Adicione mais condições de filtro conforme necessário para outros campos

        # Executa a consulta e converte os resultados para uma lista de dicionários
        records_list = [record.__dict__ for record in query.all()]

        # Remove a chave "_sa_instance_state" que não é necessária
        for record in records_list:
            record.pop('_sa_instance_state', None)

        # Converte a lista de dicionários para JSON
        records_json = json.dumps(records_list)

    return records_json