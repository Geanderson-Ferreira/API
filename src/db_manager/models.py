from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from src.db_manager.config import BASE as Base


class Hotels(Base):
    __tablename__ = 'hotels'

    HotelId = Column(Integer, primary_key=True, autoincrement=True)
    HotelName = Column(String, unique=True, nullable=False)
    locations = relationship('Locations', back_populates='Hotel')
    orders = relationship('Orders', back_populates='Hotel') 

class LocationTypes(Base):
    __tablename__ = 'location_types'

    LocationTypeId = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    LocationTypeName = Column(String, nullable=False, unique=True)

    location = relationship('Locations', back_populates='LocationTypeName')

class Locations(Base):
    __tablename__ = 'locations'

    LocationId = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    LocationType = Column(Integer, ForeignKey('location_types.LocationTypeId', name='fk_location_type', ondelete='CASCADE', deferrable=False),nullable=False)
    LocationName = Column(String, nullable=False)
    Floor = Column(Integer, nullable=False)
    HotelId = Column(Integer, ForeignKey('hotels.HotelId', name='fk_location_hotel', ondelete='CASCADE', deferrable=False))
    orders = relationship('Orders', back_populates='location')
    Hotel = relationship('Hotels')
    LocationTypeName = relationship('LocationTypes')

class Orders(Base):
    __tablename__ = 'orders'

    IdOrder = Column(Integer, primary_key=True, autoincrement=True)
    Location = Column(Integer, ForeignKey('locations.LocationId', name='fk_location', ondelete='CASCADE', deferrable=False))
    CreationDate = Column(DateTime)
    EndDate = Column(DateTime)
    OrderType = Column(Integer, ForeignKey('order_types.IDTypeOrder', name='fk_ordertype', ondelete='CASCADE', deferrable=False))
    ImageData = Column(LargeBinary, nullable=True)
    Description = Column(String)
    CreatedBy = Column(Integer, ForeignKey('users.Id', name='fk_orderType', ondelete='SET NULL', deferrable=False))
    Status = Column(Integer, ForeignKey('order_status.IdStatus', name='fk_orderstatus', ondelete='CASCADE', deferrable=False), default=1)
    HotelId = Column(Integer, ForeignKey('hotels.HotelId', name='fk_location_hotel', ondelete='CASCADE', deferrable=False))
    
    location = relationship('Locations', back_populates='orders')
    order_type = relationship('OrderTypes', back_populates='orders')
    created_by = relationship('User')
    status = relationship('OrderStatus')
    Hotel= relationship('Hotels')

class User(Base):
    __tablename__ = 'users'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String, unique=True, nullable=False)
    Password = Column(String, nullable=False, unique=True)
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