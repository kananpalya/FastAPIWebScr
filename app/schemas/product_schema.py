from pydantic import BaseModel, AnyHttpUrl
class ProductCreate(BaseModel):
    """
    Schema for requesting product scraping via its URL.

    Attributes:
        url (str): The Walmart product URL to scrape.
    """
    url: str

class ProductResponse(ProductCreate):
    """
    Schema for responding with detailed product information after scraping.

    Attributes:
        id (str): Unique identifier for the product record.
        title (str): The product title/name.
        price (str): The product price as a string.
        description (str | None): Optional product description text.
    """
    id: str
    title: str
    price: str
    description: str | None
