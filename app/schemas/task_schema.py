from pydantic import BaseModel, HttpUrl
from typing import Any
from datetime import datetime

class TaskCreate(BaseModel):
    url: HttpUrl

class TaskResponse(BaseModel):
    id: str
    url: HttpUrl
    status: str
    scraped_data: Any
