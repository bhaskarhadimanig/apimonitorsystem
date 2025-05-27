from pydantic import BaseModel
from typing import Optional

class ApiBase(BaseModel):
    name: str
    url: str
    method: str = "GET"
    frequency: int

class ApiCreate(ApiBase):
    pass

class ApiUpdate(BaseModel):
    name: Optional[str]
    url: Optional[str]
    method: Optional[str]
    frequency: Optional[int]
    is_active: Optional[bool]

class ApiOut(ApiBase):
    id: int
    is_active: bool
    class Config:
        from_attributes = True