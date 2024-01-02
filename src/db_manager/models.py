from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary, create_engine
from sqlalchemy.orm import relationship
from src.db_manager.config import DB, DB_NAME
from datetime import datetime
import os
from src.db_manager.base import Base


class Hotels(Base):
    __tablename__ = 'hotels'

    HotelId = Column(Integer, primary_key=True, autoincrement=True)
    HotelName = Column(String, unique=True, nullable=False)
    locations = relationship('Locations', back_populates='Hotel')


class Locations(Base):
    __tablename__ = 'locations'

    IDLocation = Column(Integer, primary_key=True)
    LocationType = Column(String, nullable=False)
    LocationName = Column(String, nullable=False)
    Floor = Column(Integer, nullable=False)
    HotelId = Column(Integer, ForeignKey('hotels.HotelId'))
    orders = relationship('Orders', back_populates='location')
    Hotel = relationship('Hotels')

class Orders(Base):
    __tablename__ = 'orders'

    IdOrder = Column(Integer, primary_key=True)
    Location = Column(Integer, ForeignKey('locations.IDLocation'))
    CreationDate = Column(DateTime)
    EndDate = Column(DateTime)
    OrderType = Column(Integer, ForeignKey('order_types.IDTypeOrder'))
    ImageData = Column(LargeBinary, nullable=True)
    Description = Column(String)
    CreatedBy = Column(Integer, ForeignKey('users.Id'))
    Status = Column(Integer, ForeignKey('order_status.IdStatus'), default='Pendente')
    HotelId = Column(Integer, ForeignKey('hotels.HotelId'))
    location = relationship('Locations', back_populates='orders')
    order_type = relationship('OrderTypes', back_populates='orders')
    created_by = relationship('User')
    status = relationship('OrderStatus')

class User(Base):
    __tablename__ = 'users'

    Id = Column(Integer, primary_key=True)
    Username = Column(String, unique=True, nullable=False)
    Password = Column(String, nullable=False)
    FullName = Column(String)
    Email = Column(String, unique=True, nullable=False)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
    orders = relationship('Orders', back_populates='created_by')

class OrderTypes(Base):
    __tablename__ = 'order_types'

    IDTypeOrder = Column(Integer, primary_key=True)
    OrderTypeName = Column(String, unique=True, nullable=False)
    orders = relationship('Orders', back_populates='order_type')

class OrderStatus(Base):
    __tablename__ = 'order_status'

    IdStatus = Column(Integer, primary_key=True)
    StatusName = Column(String, unique=True, nullable=False)
    orders = relationship('Orders', back_populates='status')


def create_all():
    try:
        engine = create_engine(DB)
        Base.metadata.create_all(engine)
    except:
        pass

def recreate_db():
    #Criar as tabelas
    try:
        os.remove(DB_NAME)
    except:
        pass
    create_all()
    print('>> DB+TABELAS RECRIADOS')