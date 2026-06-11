from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/drivers", tags=["drivers"])


@router.post("/", response_model=schemas.DriverRead)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db, driver)


@router.get("/", response_model=list[schemas.DriverRead])
def list_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_drivers(db, skip=skip, limit=limit)


@router.get("/{driver_id}", response_model=schemas.DriverRead)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    obj = crud.get_driver(db, driver_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Driver not found")
    return obj


@router.put("/{driver_id}", response_model=schemas.DriverRead)
def update_driver(driver_id: int, data: schemas.DriverCreate, db: Session = Depends(get_db)):
    obj = crud.update_driver(db, driver_id, data.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Driver not found")
    return obj


@router.delete("/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_driver(db, driver_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"ok": True}
