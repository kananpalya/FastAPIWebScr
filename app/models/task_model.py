from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

class TaskDB(BaseModel):
    email: EmailStr
    url: str
    status: str = "pending"
    result: Optional[Dict] = None
