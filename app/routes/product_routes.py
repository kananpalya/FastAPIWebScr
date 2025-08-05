# from fastapi import APIRouter, HTTPException, BackgroundTasks
# from pydantic import BaseModel
# from app.db import get_db
# from app.services.scraping_service import scrape_product_task
# from bson.objectid import ObjectId

# router = APIRouter()

# class ProductScrapeRequest(BaseModel):
#     url: str

# @router.post("/scrape")
# def scrape_product_api(req: ProductScrapeRequest, background_tasks: BackgroundTasks):
#     db = get_db()
#     # Create task entry
#     task_doc = {
#         "product_url": req.url,
#         "status": "pending"
#     }
#     result = db["tasks"].insert_one(task_doc)
#     task_id = str(result.inserted_id)
#     # Start background scraping task
#     background_tasks.add_task(scrape_product_task, task_id, req.url)
#     return {"message": "Scraping started", "task_id": task_id}





from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.db import get_db
from app.services.scraping_service import scrape_product_task
from bson.objectid import ObjectId


router = APIRouter()


class ProductScrapeRequest(BaseModel):
    """
    Schema for the product scrape request payload.

    Attributes:
        url (str): The URL of the product page to scrape.
    """
    url: str


@router.post("/scrape")
def scrape_product_api(req: ProductScrapeRequest, background_tasks: BackgroundTasks):
    """
    Endpoint to start a background scraping task for a given product URL.

    This endpoint inserts a new task document into the database with status "pending"
    and then schedules the scraping function to run asynchronously in the background.

    Args:
        req (ProductScrapeRequest): Request body containing the product URL.
        background_tasks (BackgroundTasks): FastAPI BackgroundTasks instance to run tasks asynchronously.

    Returns:
        dict: A JSON response containing a success message and the created task ID.
    """
    db = get_db()
    # Create task entry
    task_doc = {
        "product_url": req.url,
        "status": "pending"
    }
    result = db["tasks"].insert_one(task_doc)
    task_id = str(result.inserted_id)
    # Start background scraping task
    background_tasks.add_task(scrape_product_task, task_id, req.url)
    return {"message": "Scraping started", "task_id": task_id}
