from sqlalchemy.orm import sessionmaker
from src.db_manager.config import SESSION
from datetime import datetime
from src.db_manager.models import Orders
# ... (seu código para configurar o SQLAlchemy e as tabelas)

# Criar uma sessão
Session = SESSION
session = Session()

from sqlalchemy import text

# ...

try:
    # Tente inserir manualmente uma ordem com um HotelId que não existe
    session.execute(text("INSERT INTO orders (Location, CreationDate, EndDate, OrderType, HotelId, Description, CreatedBy) VALUES (1, :creation_date, :end_date, 1, 999, 'Test Order', 1)"), {'creation_date': datetime.now(), 'end_date': datetime.now()})
    session.commit()
except Exception as e:
    session.rollback()
    print(f"Erro ao inserir ordem manualmente: {e}")
finally:
    session.close()

"""
try:
    # Tentar inserir uma ordem com IdHotel que não existe
    new_order = Orders(Location=1, CreationDate=datetime.now(), EndDate=datetime.now(), OrderType=1, HotelId=999, Description="Test Order", CreatedBy=1)
    session.add(new_order)
    session.commit()
except Exception as e:
    session.rollback()
    print(f"Erro ao inserir ordem: {e}")
finally:
    session.close()
"""