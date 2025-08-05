# # File: app/schemas/product_schema.py

# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime

# class Product(BaseModel):
#     url: str
#     title: str
#     price: str
#     description: Optional[str] = ""
#     scraped_at: datetime

#     class Config:
#         orm_mode = True
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    """
    Schema representing a scraped product.

    Attributes:
        url (str): The URL of the product page.
        title (str): The title or name of the product.
        price (str): The price of the product as a string.
        description (Optional[str]): An optional description of the product. Defaults to an empty string if not provided.
        scraped_at (datetime): The datetime when the product data was scraped.
    """

    url: str
    title: str
    price: str
    description: Optional[str] = ""
    scraped_at: datetime

    class Config:
        """
        Pydantic configuration for ORM mode.

        Enables compatibility with ORM objects, allowing Pydantic to read data
        from database models or any class with attributes.
        """
        orm_mode = True
