from pydantic import BaseModel

class Product(BaseModel):
    task_id: str
    title: str
    price: float
    image: str
    url: str
