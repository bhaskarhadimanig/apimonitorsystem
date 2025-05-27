from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import get_admin_user
from app.db.session import get_db
from app.crud import crud_user

router = APIRouter()

@router.get("/users")
def list_users(db: Session = Depends(get_db), current_user=Depends(get_admin_user)):
    return crud_user.get_users(db)

@router.put("/users/{user_id}/role")
def set_role(user_id: int, role: str, db: Session = Depends(get_db), current_user=Depends(get_admin_user)):
    user = crud_user.set_user_role(db, user_id, role)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user