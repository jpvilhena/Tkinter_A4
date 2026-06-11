from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Text,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Association tables for many-to-many relationships between services and resources
service_trucks = Table(
    'service_trucks',
    Base.metadata,
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True),
    Column('truck_id', Integer, ForeignKey('trucks.id'), primary_key=True),
)

service_drivers = Table(
    'service_drivers',
    Base.metadata,
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True),
    Column('driver_id', Integer, ForeignKey('drivers.id'), primary_key=True),
)

service_helpers = Table(
    'service_helpers',
    Base.metadata,
    Column('service_id', Integer, ForeignKey('services.id'), primary_key=True),
    Column('helper_id', Integer, ForeignKey('helpers.id'), primary_key=True),
)


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(Text, nullable=True)
    services = relationship('Service', back_populates='client')


class Truck(Base):
    __tablename__ = 'trucks'
    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String(50), unique=True, nullable=False)
    model = Column(String(100), nullable=True)
    capacity = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)
    services = relationship('Service', secondary=service_trucks, back_populates='trucks')


class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    cpf = Column(String(50), nullable=True)
    license = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=True)
    services = relationship('Service', secondary=service_drivers, back_populates='drivers')


class Helper(Base):
    __tablename__ = 'helpers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(50), nullable=True)
    daily_rate = Column(String(50), nullable=True)
    services = relationship('Service', secondary=service_helpers, back_populates='helpers')


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    origin = Column(Text, nullable=False)
    destination = Column(Text, nullable=False)
    box_count = Column(Integer, nullable=False)
    service_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)

    client = relationship('Client', back_populates='services')
    trucks = relationship('Truck', secondary=service_trucks, back_populates='services')
    drivers = relationship('Driver', secondary=service_drivers, back_populates='services')
    helpers = relationship('Helper', secondary=service_helpers, back_populates='services')
