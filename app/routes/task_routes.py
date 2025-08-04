from fastapi import APIRouter, HTTPException, status, Body
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.scraping_service import scrape_product_data
from app.db import get_mongo_collection
from bson import ObjectId
from datetime import datetime
import asyncio
import logging
import time

router = APIRouter()
logging.basicConfig(level=logging.INFO)

tasks_collection = get_mongo_collection("tasks")

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_scraping_task(task: TaskCreate = Body(...)):
    logging.info(f"Scraping task received for URL: {task.url}")

    try:
        start_time = time.time()
        # Run scraper in a thread with timeout
        scraped_data = await asyncio.wait_for(
            asyncio.to_thread(scrape_product_data, task.url),
            timeout=15.0
        )
        logging.info(f"Scraping completed in {time.time() - start_time:.2f}s")

        task_doc = {
            "url": task.url,
            "scraped_data": scraped_data,
            "status": "successful",
            "created_at": datetime.utcnow()
        }
        result = tasks_collection.insert_one(task_doc)

        return TaskResponse(
            id=str(result.inserted_id),
            url=task.url,
            status=task_doc["status"],
            scraped_data=scraped_data
        )

    except asyncio.TimeoutError:
        logging.error("Scraping timed out")
        raise HTTPException(status_code=504, detail="Scraping timed out")
    except Exception as e:
        logging.exception("Unexpected error during scraping")
        raise HTTPException(status_code=500, detail="Internal server error")
