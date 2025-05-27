from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.settings import EmailSettingsUpdate, EmailSettingsOut
from app.crud import crud_settings
from app.core.security import get_current_user
from app.db.session import get_db

router = APIRouter()

# @router.get("/email", response_model=EmailSettingsOut)
# def get_email_settings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     return crud_settings.get_email_settings(db, current_user.id)
@router.get("/email", response_model=EmailSettingsOut)
def get_email_settings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    settings = crud_settings.get_email_settings(db, current_user.id)
    if settings and (not settings.from_email or '@' not in settings.from_email):
        settings.from_email = "bhadimanig@gmail.com"
    return settings

@router.put("/email", response_model=EmailSettingsOut)
def update_email_settings(settings_in: EmailSettingsUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_settings.update_email_settings(db, current_user.id, settings_in)