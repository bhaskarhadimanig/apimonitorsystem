from pydantic import BaseModel, EmailStr

class EmailSettingsUpdate(BaseModel):
    from_email: EmailStr

class EmailSettingsOut(BaseModel):
    from_email: EmailStr
    class Config:
        from_attributes = True