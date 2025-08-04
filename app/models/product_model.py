from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class ProductModel(BaseModel):
    """
    Product database model schema for MongoDB documents representing Walmart products scraped.

    Attributes:
        id (str): Unique identifier of the product (MongoDB ObjectId as string, aliased as "_id").
        title (str): Title or name of the product.
        price (str): Price of the product as a string.
        url (str): URL of the product page.
        description (str | None): Optional product description text.
    """
    id: str = Field(default_factory=str, alias="_id")
    title: str
    price: str
    url: str
    description: str | None = None

    class Config:
        """
        Pydantic configuration for ORM compatibility and alias support.
        """
        orm_mode = True
        allow_population_by_field_name = True
