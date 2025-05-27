from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserLogin, UserUpdate
from app.crud import crud_user
from app.core.security import verify_password, create_access_token, get_current_user
from app.db.session import get_db

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud_user.create_user(db, user_in)
    return user

@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, user_in.email)
    if not db_user or not verify_password(user_in.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = create_access_token({"sub": db_user.email, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserOut)
def update_me(user_update: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_user.update_user(db, current_user, user_update)