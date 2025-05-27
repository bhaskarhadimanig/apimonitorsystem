import smtplib
from email.message import EmailMessage
from app.core.config import settings

def send_email(subject: str, body: str, to: list, from_addr=None):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = from_addr or settings.SMTP_USER
    msg["To"] = ", ".join(to)
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)