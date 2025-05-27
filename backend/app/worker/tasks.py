from celery import Celery
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.api import Api
from app.models.apirequest import ApiRequest
from app.services.email import send_email
from app.models.email_group import EmailGroup, Email
from app.models.email_settings import EmailSettings
import requests
from datetime import datetime

celery = Celery("worker", broker=settings.REDIS_BROKER_URL)

@celery.task
def check_api(api_id: int):
    db = SessionLocal()
    api = db.query(Api).get(api_id)
    if not api or not api.is_active:
        db.close()
        return
    try:
        start = datetime.utcnow()
        response = requests.request(api.method, api.url, timeout=15)
        duration = int((datetime.utcnow() - start).total_seconds() * 1000)
        status = "success" if response.status_code < 400 else "fail"
        code = response.status_code
    except Exception:
        duration = None
        status = "fail"
        code = None
    req = ApiRequest(
        api_id=api.id,
        status=status,
        response_code=code,
        response_time=duration,
        checked_at=datetime.utcnow(),
    )
    db.add(req)
    db.commit()
    # Notify on failure
    if status == "fail":
        emails = []
        for group in api.email_groups:
            for email in group.emails:
                emails.append(email.email)
        if not emails:
            emails = [api.owner.email]
        settings_row = db.query(EmailSettings).filter(EmailSettings.user_id == api.owner_id).first()
        from_email = settings_row.from_email if settings_row else api.owner.email
        send_email(
            subject=f"API DOWN: {api.name}",
            body=f"API {api.name} ({api.url}) is DOWN.",
            to=emails,
            from_addr=from_email
        )
    db.close()