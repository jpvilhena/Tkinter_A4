from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_client(db: Session, client: schemas.ClientCreate):
    db_obj = models.Client(**client.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def list_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def update_client(db: Session, client_id: int, data: dict):
    db_obj = get_client(db, client_id)
    if not db_obj:
        return None
    for k, v in data.items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_client(db: Session, client_id: int):
    db_obj = get_client(db, client_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return True


# Trucks
def create_truck(db: Session, truck: schemas.TruckCreate):
    db_obj = models.Truck(**truck.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_truck(db: Session, truck_id: int):
    return db.query(models.Truck).filter(models.Truck.id == truck_id).first()


def list_trucks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Truck).offset(skip).limit(limit).all()


def update_truck(db: Session, truck_id: int, data: dict):
    db_obj = get_truck(db, truck_id)
    if not db_obj:
        return None
    for k, v in data.items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_truck(db: Session, truck_id: int):
    db_obj = get_truck(db, truck_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return True


# Drivers
def create_driver(db: Session, driver: schemas.DriverCreate):
    db_obj = models.Driver(**driver.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()


def list_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()


def update_driver(db: Session, driver_id: int, data: dict):
    db_obj = get_driver(db, driver_id)
    if not db_obj:
        return None
    for k, v in data.items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_driver(db: Session, driver_id: int):
    db_obj = get_driver(db, driver_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return True


# Helpers
def create_helper(db: Session, helper: schemas.HelperCreate):
    db_obj = models.Helper(**helper.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_helper(db: Session, helper_id: int):
    return db.query(models.Helper).filter(models.Helper.id == helper_id).first()


def list_helpers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Helper).offset(skip).limit(limit).all()


def update_helper(db: Session, helper_id: int, data: dict):
    db_obj = get_helper(db, helper_id)
    if not db_obj:
        return None
    for k, v in data.items():
        setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_helper(db: Session, helper_id: int):
    db_obj = get_helper(db, helper_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return True


# Services
def create_service(db: Session, service: schemas.ServiceCreate):
    data = service.dict()
    truck_ids = data.pop('truck_ids', []) or []
    driver_ids = data.pop('driver_ids', []) or []
    helper_ids = data.pop('helper_ids', []) or []

    db_obj = models.Service(**data)
    # attach relations after adding
    if truck_ids:
        db_obj.trucks = db.query(models.Truck).filter(models.Truck.id.in_(truck_ids)).all()
    if driver_ids:
        db_obj.drivers = db.query(models.Driver).filter(models.Driver.id.in_(driver_ids)).all()
    if helper_ids:
        db_obj.helpers = db.query(models.Helper).filter(models.Helper.id.in_(helper_ids)).all()

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_service(db: Session, service_id: int):
    return db.query(models.Service).filter(models.Service.id == service_id).first()


def list_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()


def update_service(db: Session, service_id: int, data: dict):
    db_obj = get_service(db, service_id)
    if not db_obj:
        return None
    # handle simple fields
    simple_fields = ['origin', 'destination', 'box_count', 'service_date', 'notes', 'client_id']
    for f in simple_fields:
        if f in data:
            setattr(db_obj, f, data[f])
    # relations
    if 'truck_ids' in data:
        ids = data.get('truck_ids') or []
        db_obj.trucks = db.query(models.Truck).filter(models.Truck.id.in_(ids)).all()
    if 'driver_ids' in data:
        ids = data.get('driver_ids') or []
        db_obj.drivers = db.query(models.Driver).filter(models.Driver.id.in_(ids)).all()
    if 'helper_ids' in data:
        ids = data.get('helper_ids') or []
        db_obj.helpers = db.query(models.Helper).filter(models.Helper.id.in_(ids)).all()

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_service(db: Session, service_id: int):
    db_obj = get_service(db, service_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return True
