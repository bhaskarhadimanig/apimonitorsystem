from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.monitor import ApiMonitorOut
from app.crud import crud_monitor
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/history/{api_id}", response_model=list[ApiMonitorOut])
def get_api_history(api_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_monitor.get_api_history(db, api_id, current_user.id)

@router.get("/stats", response_model=dict)
def get_stats(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud_monitor.get_user_stats(db, current_user.id)