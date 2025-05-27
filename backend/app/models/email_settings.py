from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class EmailSettings(Base):
    __tablename__ = "email_settings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    from_email = Column(String, nullable=False)
    user = relationship("User", back_populates="email_settings")