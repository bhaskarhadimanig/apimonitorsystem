from pydantic import BaseModel
from typing import List

class EmailBase(BaseModel):
    email: str

class EmailCreate(EmailBase):
    pass

class EmailOut(EmailBase):
    id: int
    class Config:
        from_attributes = True

class EmailGroupBase(BaseModel):
    name: str

class EmailGroupCreate(EmailGroupBase):
    emails: List[EmailCreate]

class EmailGroupUpdate(BaseModel):
    name: str
    emails: List[EmailCreate]

class EmailGroupOut(EmailGroupBase):
    id: int
    emails: List[EmailOut]
    class Config:
        from_attributes = True