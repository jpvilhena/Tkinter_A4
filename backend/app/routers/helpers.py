from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/helpers", tags=["helpers"])


@router.post("/", response_model=schemas.HelperRead)
def create_helper(helper: schemas.HelperCreate, db: Session = Depends(get_db)):
    return crud.create_helper(db, helper)


@router.get("/", response_model=list[schemas.HelperRead])
def list_helpers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_helpers(db, skip=skip, limit=limit)


@router.get("/{helper_id}", response_model=schemas.HelperRead)
def get_helper(helper_id: int, db: Session = Depends(get_db)):
    obj = crud.get_helper(db, helper_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Helper not found")
    return obj


@router.put("/{helper_id}", response_model=schemas.HelperRead)
def update_helper(helper_id: int, data: schemas.HelperCreate, db: Session = Depends(get_db)):
    obj = crud.update_helper(db, helper_id, data.dict())
    if not obj:
        raise HTTPException(status_code=404, detail="Helper not found")
    return obj


@router.delete("/{helper_id}")
def delete_helper(helper_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_helper(db, helper_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Helper not found")
    return {"ok": True}
