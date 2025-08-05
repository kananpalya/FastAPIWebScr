# from fastapi import APIRouter, BackgroundTasks, HTTPException
# from app.schemas.task_schema import TaskCreate, TaskResponse
# from app.services.scraping_service import scrape_product_task
# from app.db import get_db
# import logging
# from app.utils.exceptions import BadRequestException, ConflictException

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/scrape/", response_model=TaskResponse)
# def start_scraping(task: TaskCreate, background_tasks: BackgroundTasks):
#     """
#     Start a background scraping task for a given Walmart product URL.

#     Args:
#         task (TaskCreate): Contains the product URL and task creation timestamp.
#         background_tasks (BackgroundTasks): FastAPI background task manager.

#     Returns:
#         TaskResponse: Task details including ID, status, and timestamps.

#     Raises:
#         BadRequestException: If required fields are missing or invalid.
#         ConflictException: If a similar pending task already exists.
#         HTTPException: If task creation or database operation fails.
#     """
#     db = get_db()

#     # Validate input
#     if not task.product_url or not task.product_url.startswith("http"):
#         raise BadRequestException(detail="Invalid or missing product URL.")

#     try:
#         # Optional: Check if a pending task for the same URL already exists
#         existing_task = db["tasks"].find_one({
#             "product_url": task.product_url,
#             "status": "pending"
#         })
#         if existing_task:
#             raise ConflictException(detail="A pending scraping task for this product URL already exists.")

#         # Insert new task as "pending"
#         new_task = {
#             "product_url": task.product_url,
#             "status": "pending",
#             "created_at": task.created_at,
#             "finished_at": None,
#         }
#         result = db["tasks"].insert_one(new_task)
#         task_id = str(result.inserted_id)
#         background_tasks.add_task(scrape_product_task, task_id, task.product_url)
#         new_task["id"] = task_id
#         return TaskResponse(**new_task)
#     except (BadRequestException, ConflictException):
#         raise
#     except Exception as e:
#         logger.error(f"Failed to start scraping task: {e}")
#         raise HTTPException(status_code=500, detail="Internal server error when starting scraping task")




















# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from app.db import get_db

# router = APIRouter()

# class TaskCreate(BaseModel):
#     task_name: str
#     initiated_by: str

# @router.post("/create")
# def create_task(task: TaskCreate):
#     db = get_db()
#     db["tasks"].insert_one(task.dict())
#     return {"message": "Task created successfully", "task": task}
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import get_db


router = APIRouter()


class TaskCreate(BaseModel):
    """
    Schema for creating a new task.

    Attributes:
        task_name (str): The name of the task to be created.
        initiated_by (str): The identifier (e.g., username) of who initiated the task.
    """
    task_name: str
    initiated_by: str


@router.post("/create")
def create_task(task: TaskCreate):
    """
    Create a new task in the database.

    Inserts a new document representing the task into the 'tasks' collection.

    Args:
        task (TaskCreate): The task details to be created.

    Returns:
        dict: A confirmation message and the task data that was created.
    """
    db = get_db()
    db["tasks"].insert_one(task.dict())
    return {"message": "Task created successfully", "task": task}
