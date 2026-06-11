from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/", response_model=schemas.ClientRead)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)


@router.get("/", response_model=list[schemas.ClientRead])
def list_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_clients(db, skip=skip, limit=limit)


@router.get("/{client_id}", response_model=schemas.ClientRead)
def get_client(client_id: int, db: Session = Depends(get_db)):
    obj = crud.get_client(db, client_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj


@router.put("/{client_id}", response_model=schemas.ClientRead)
def update_client(client_id: int, data: schemas.ClientCreate, db: Session = Depends(get_db)):
    obj = crud.update_client(db, client_id, data.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Client not found")
    return obj


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_client(db, client_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"ok": True}
