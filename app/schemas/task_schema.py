from pydantic import BaseModel, AnyHttpUrl
from datetime import datetime
class TaskCreate(BaseModel):
    """
    Schema for creating a new scraping task.

    Attributes:
        product_url (str): The URL of the Walmart product to be scraped.
        created_at (str): ISO format timestamp when the task is created. Defaults to current UTC time.
    """
    product_url: str
    created_at: str = datetime.utcnow().isoformat()

class TaskResponse(TaskCreate):
    """
    Schema for responding with scraping task details including status and completion time.

    Attributes:
        id (str): Unique identifier for the task.
        status (str): Current status of the task (e.g., "pending", "successful", "failed").
        finished_at (str | None): ISO format timestamp when the task finished, or None if not finished.
    """
    id: str
    status: str
    finished_at: str | None = None
