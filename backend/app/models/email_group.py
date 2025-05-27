from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base

api_group_link = Table(
    'api_group_link',
    Base.metadata,
    Column('api_id', Integer, ForeignKey('apis.id')),
    Column('group_id', Integer, ForeignKey('email_groups.id'))
)

class EmailGroup(Base):
    __tablename__ = "email_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="groups")
    emails = relationship("Email", back_populates="group", cascade="all, delete")
    apis = relationship("Api", secondary=api_group_link, back_populates="email_groups")

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("email_groups.id"))
    group = relationship("EmailGroup", back_populates="emails")