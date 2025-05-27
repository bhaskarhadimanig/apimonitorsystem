from sqlalchemy.orm import Session
from app.models.email_settings import EmailSettings
from app.schemas.settings import EmailSettingsUpdate

def get_email_settings(db: Session, user_id: int):
    settings = db.query(EmailSettings).filter(EmailSettings.user_id == user_id).first()
    if not settings:
        return EmailSettings(from_email="")
    return settings

def update_email_settings(db: Session, user_id: int, settings_in: EmailSettingsUpdate):
    settings = db.query(EmailSettings).filter(EmailSettings.user_id == user_id).first()
    if not settings:
        settings = EmailSettings(user_id=user_id, from_email=settings_in.from_email)
        db.add(settings)
    else:
        settings.from_email = settings_in.from_email
    db.commit()
    db.refresh(settings)
    return settings