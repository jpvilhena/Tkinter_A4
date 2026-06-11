from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/services", tags=["services"])


@router.post("/", response_model=schemas.ServiceRead)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    # ensure client exists
    client = crud.get_client(db, service.client_id)
    if not client:
        raise HTTPException(status_code=400, detail="Client must exist before creating a service")
    return crud.create_service(db, service)


@router.get("/", response_model=list[schemas.ServiceRead])
def list_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_services(db, skip=skip, limit=limit)


@router.get("/{service_id}", response_model=schemas.ServiceRead)
def get_service(service_id: int, db: Session = Depends(get_db)):
    obj = crud.get_service(db, service_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Service not found")
    return obj


@router.put("/{service_id}", response_model=schemas.ServiceRead)
def update_service(service_id: int, data: schemas.ServiceCreate, db: Session = Depends(get_db)):
    obj = crud.update_service(db, service_id, data.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Service not found or client missing")
    return obj


@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_service(db, service_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"ok": True}
