from pydantic import BaseModel
from typing import Dict

class ProductDB(BaseModel):
    url: str
    data: Dict
