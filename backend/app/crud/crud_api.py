from sqlalchemy.orm import Session
from app.models.api import Api
from app.schemas.api import ApiCreate, ApiUpdate

def create_api(db: Session, api_in: ApiCreate, owner_id: int):
    api = Api(**api_in.dict(), owner_id=owner_id)
    db.add(api)
    db.commit()
    db.refresh(api)
    return api

def get_apis_by_user(db: Session, user_id: int):
    return db.query(Api).filter(Api.owner_id == user_id).all()

def get_api(db: Session, api_id: int, owner_id: int):
    return db.query(Api).filter(Api.id == api_id, Api.owner_id == owner_id).first()

def update_api(db: Session, api_id: int, owner_id: int, api_update: ApiUpdate):
    api = get_api(db, api_id, owner_id)
    if not api:
        return None
    for k, v in api_update.dict(exclude_unset=True).items():
        setattr(api, k, v)
    db.commit()
    db.refresh(api)
    return api

def delete_api(db: Session, api_id: int, owner_id: int):
    api = get_api(db, api_id, owner_id)
    if api:
        db.delete(api)
        db.commit()