from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    username: str
    created_at: datetime
