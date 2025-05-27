from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.api import ApiCreate, ApiUpdate, ApiOut
from app.crud import crud_api
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=ApiOut)
def create_api(api_in: ApiCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    api = crud_api.create_api(db, api_in, current_user.id)
    return api

@router.get("/", response_model=list[ApiOut])
def get_apis(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_api.get_apis_by_user(db, current_user.id)

@router.get("/{api_id}", response_model=ApiOut)
def get_api(api_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    api = crud_api.get_api(db, api_id, current_user.id)
    if not api:
        raise HTTPException(status_code=404, detail="API not found")
    return api

@router.put("/{api_id}", response_model=ApiOut)
def update_api(api_id: int, api_update: ApiUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_api.update_api(db, api_id, current_user.id, api_update)

@router.delete("/{api_id}")
def delete_api(api_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    crud_api.delete_api(db, api_id, current_user.id)
    return {"ok": True}