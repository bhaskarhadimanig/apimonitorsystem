from sqlalchemy.orm import Session
from app.models.email_group import EmailGroup, Email
from app.schemas.email_group import EmailGroupCreate, EmailGroupUpdate

def create_group(db: Session, group_in: EmailGroupCreate, owner_id: int):
    group = EmailGroup(name=group_in.name, owner_id=owner_id)
    db.add(group)
    db.commit()
    db.refresh(group)
    for email_in in group_in.emails:
        email = Email(email=email_in.email, group_id=group.id)
        db.add(email)
    db.commit()
    db.refresh(group)
    return group

def get_groups_by_user(db: Session, owner_id: int):
    return db.query(EmailGroup).filter(EmailGroup.owner_id == owner_id).all()

def update_group(db: Session, group_id: int, owner_id: int, group_update: EmailGroupUpdate):
    group = db.query(EmailGroup).filter(EmailGroup.id == group_id, EmailGroup.owner_id == owner_id).first()
    if not group:
        return None
    group.name = group_update.name
    db.query(Email).filter(Email.group_id == group_id).delete()
    for email_in in group_update.emails:
        db.add(Email(email=email_in.email, group_id=group_id))
    db.commit()
    db.refresh(group)
    return group

def delete_group(db: Session, group_id: int, owner_id: int):
    group = db.query(EmailGroup).filter(EmailGroup.id == group_id, EmailGroup.owner_id == owner_id).first()
    if group:
        db.delete(group)
        db.commit()