from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.email_group import EmailGroupCreate, EmailGroupOut, EmailGroupUpdate
from app.crud import crud_email_group
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=EmailGroupOut)
def create_group(group_in: EmailGroupCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_email_group.create_group(db, group_in, current_user.id)

@router.get("/", response_model=list[EmailGroupOut])
def get_groups(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_email_group.get_groups_by_user(db, current_user.id)

@router.put("/{group_id}", response_model=EmailGroupOut)
def update_group(group_id: int, group_update: EmailGroupUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_email_group.update_group(db, group_id, current_user.id, group_update)

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    crud_email_group.delete_group(db, group_id, current_user.id)
    return {"ok": True}