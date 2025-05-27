from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class ApiRequest(Base):
    __tablename__ = "api_requests"
    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, ForeignKey("apis.id"))
    status = Column(String, nullable=False)  # "success" / "fail"
    response_code = Column(Integer, nullable=True)
    response_time = Column(Integer, nullable=True)  # ms
    checked_at = Column(DateTime, nullable=False)
    api = relationship("Api", back_populates="requests")