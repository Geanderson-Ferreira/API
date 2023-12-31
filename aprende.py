"""
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from DB_MANAGER.models import Orders

# Substitua 'sqlite:///example.db' pelo URL do seu banco de dados
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Consulta para contar o número de linhas para cada tipo de ordem
order_counts = (
    session.query(Orders.OrderType, func.count(Orders.IdOrder))
    .filter(Orders.Status==2)
    .group_by(Orders.OrderType)
    .all()
)

# Exibindo os resultados
for order_type, count in order_counts:
    print(f"OrderType {order_type}: {count} linhas")
"""
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from DB_MANAGER.models import Orders, OrderTypes  # Certifique-se de importar as classes do seu módulo
import json

# Substitua 'sqlite:///example.db' pelo URL do seu banco de dados
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Consulta usando JOIN para obter OrderTypeName diretamente
order_counts = (
    session.query(OrderTypes.OrderTypeName, func.count(Orders.IdOrder))
    .join(Orders, OrderTypes.IDTypeOrder == Orders.OrderType)
    .filter(Orders.Status == 2)
    .group_by(OrderTypes.OrderTypeName)
    .all()
)

# Criando um dicionário para armazenar os resultados
result_dict = {"order_counts": [{"OrderTypeName": order_type, "Count": count} for order_type, count in order_counts]}

# Convertendo o dicionário em uma string JSON
result_json = json.dumps(result_dict, indent=2)

# Exibindo a string JSON
print(result_json)
