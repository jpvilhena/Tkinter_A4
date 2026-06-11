from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/trucks", tags=["trucks"])


@router.post("/", response_model=schemas.TruckRead)
def create_truck(truck: schemas.TruckCreate, db: Session = Depends(get_db)):
    return crud.create_truck(db, truck)


@router.get("/", response_model=list[schemas.TruckRead])
def list_trucks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_trucks(db, skip=skip, limit=limit)


@router.get("/{truck_id}", response_model=schemas.TruckRead)
def get_truck(truck_id: int, db: Session = Depends(get_db)):
    obj = crud.get_truck(db, truck_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Truck not found")
    return obj


@router.put("/{truck_id}", response_model=schemas.TruckRead)
def update_truck(truck_id: int, data: schemas.TruckCreate, db: Session = Depends(get_db)):
    obj = crud.update_truck(db, truck_id, data.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Truck not found")
    return obj


@router.delete("/{truck_id}")
def delete_truck(truck_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_truck(db, truck_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Truck not found")
    return {"ok": True}
