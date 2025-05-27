from sqlalchemy.orm import Session
from app.models.apirequest import ApiRequest

def get_api_history(db: Session, api_id: int, owner_id: int):
    return db.query(ApiRequest).join(ApiRequest.api).filter(ApiRequest.api_id == api_id, ApiRequest.api.has(owner_id=owner_id)).order_by(ApiRequest.checked_at.desc()).all()

def get_user_stats(db: Session, user_id: int):
    # Example: average response time, last status per API
    from sqlalchemy import func
    apis = db.query(ApiRequest.api_id, func.avg(ApiRequest.response_time).label("avg_time")).join(ApiRequest.api).filter(ApiRequest.api.has(owner_id=user_id)).group_by(ApiRequest.api_id).all()
    return {"responseTimes": [{"api_id": a.api_id, "avg": a.avg_time} for a in apis]}