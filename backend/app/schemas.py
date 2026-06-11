from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime


class ClientBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True


class TruckBase(BaseModel):
    plate: str
    model: Optional[str] = None
    capacity: Optional[str] = None
    notes: Optional[str] = None


class TruckCreate(TruckBase):
    pass


class TruckRead(TruckBase):
    id: int

    class Config:
        orm_mode = True


class DriverBase(BaseModel):
    name: str
    cpf: Optional[str] = None
    license: str
    phone: Optional[str] = None


class DriverCreate(DriverBase):
    pass


class DriverRead(DriverBase):
    id: int

    class Config:
        orm_mode = True


class HelperBase(BaseModel):
    name: str
    phone: Optional[str] = None
    daily_rate: Optional[str] = None


class HelperCreate(HelperBase):
    pass


class HelperRead(HelperBase):
    id: int

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    client_id: int
    origin: str
    destination: str
    box_count: int
    service_date: date
    notes: Optional[str] = None


class ServiceCreate(ServiceBase):
    truck_ids: Optional[List[int]] = []
    driver_ids: Optional[List[int]] = []
    helper_ids: Optional[List[int]] = []


class ServiceRead(ServiceBase):
    id: int
    created_at: Optional[datetime]
    trucks: List[TruckRead] = []
    drivers: List[DriverRead] = []
    helpers: List[HelperRead] = []

    class Config:
        orm_mode = True
