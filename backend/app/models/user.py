from sqlalchemy import Column, String, Integer, Boolean, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
    apis = relationship("Api", back_populates="owner")
    email_settings = relationship("EmailSettings", uselist=False, back_populates="user")
    groups = relationship("EmailGroup", back_populates="owner")