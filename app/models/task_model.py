from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class TaskModel(BaseModel):
    """
    Task database model schema for MongoDB documents representing scraping tasks.

    Attributes:
        id (str): Unique identifier of the task (MongoDB ObjectId as string, aliased as "_id").
        product_url (str): The URL of the product to be scraped.
        status (str): Current status of the task (e.g., "pending", "successful", "failed").
        created_at (str): ISO formatted timestamp when the task was created.
        finished_at (str | None): ISO formatted timestamp when the task finished or None if ongoing.
    """
    id: str = Field(default_factory=str, alias="_id")
    product_url: str
    status: str
    created_at: str
    finished_at: str | None = None

    class Config:
        """
        Pydantic configuration for ORM compatibility and alias support.
        """
        orm_mode = True
        allow_population_by_field_name = True
