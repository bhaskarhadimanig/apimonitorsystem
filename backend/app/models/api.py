from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Api(Base):
    __tablename__ = "apis"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    method = Column(String, default="GET")
    frequency = Column(Integer, nullable=False, default=60)  # seconds
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="apis")
    requests = relationship("ApiRequest", back_populates="api", cascade="all, delete")
    email_groups = relationship("EmailGroup", secondary="api_group_link", back_populates="apis")