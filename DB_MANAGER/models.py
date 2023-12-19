from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from DB_MANAGER.config import DB
from datetime import datetime

Base = declarative_base()


class Hotels(Base):
    __tablename__ = 'hotels'

    HotelId = Column(Integer, primary_key=True, autoincrement=True)
    HotelName = Column(String, unique=True, nullable=False)

    # Define as relações
    locations = relationship('Locations', back_populates='hotel')


class Locations(Base):
    __tablename__ = 'locations'

    IDLocation = Column(Integer, primary_key=True)
    LocationType = Column(String, nullable=False)
    LocationName = Column(String, nullable=False)
    Floor = Column(Integer, nullable=False)
    HotelId = Column(Integer, ForeignKey('hotels.HotelId'))

    # Define as relações
    orders = relationship('Orders', back_populates='location')
    hotel = relationship('Hotels')

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

    # Define as relações
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
    # Define as relações
    orders = relationship('Orders', back_populates='created_by')

class OrderTypes(Base):
    __tablename__ = 'order_types'

    IDTypeOrder = Column(Integer, primary_key=True)
    OrderTypeName = Column(String, unique=True, nullable=False)

    # Define as relações
    orders = relationship('Orders', back_populates='order_type')

class OrderStatus(Base):
    __tablename__ = 'order_status'

    IdStatus = Column(Integer, primary_key=True)
    StatusName = Column(String, unique=True, nullable=False)


    # Define as relações
    orders = relationship('Orders', back_populates='status')


def create_all():
    try:
        engine = create_engine(DB)
        Base.metadata.create_all(engine)
    except:
        pass
