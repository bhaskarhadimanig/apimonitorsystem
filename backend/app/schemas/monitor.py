from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ApiMonitorOut(BaseModel):
    id: int
    status: str
    response_code: Optional[int]
    response_time: Optional[int]
    checked_at: datetime

    class Config:
        from_attributes = True