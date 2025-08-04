import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from app.db import get_db
import logging
from bson.objectid import ObjectId
from bson.errors import InvalidId
from requests.exceptions import RequestException


logger = logging.getLogger(__name__)


def scrape_product_task(task_id: str, url: str) -> None:
    """
    Background task that scrapes product data from a Walmart product URL and updates task status in MongoDB.
    
    This function performs the following steps:
        - Validate the task_id to ensure it is a valid MongoDB ObjectId.
        - Fetch the Walmart product page HTML content using an HTTP GET request with browser-like headers.
        - Parse the HTML to extract product title, price, and description.
        - Insert the scraped product data into the 'products' collection in MongoDB.
        - Update the associated scraping task document in the 'tasks' collection to reflect the status ('successful' or 'failed')
          and record the finish time and any error messages.
        - Log detailed information and any errors encountered for monitoring and debugging.

    Args:
        task_id (str): The string representation of the MongoDB ObjectId corresponding to the scraping task.
        url (str): The URL of the Walmart product page to scrape.

    Returns:
        None
    """
    db = get_db()
    try:
        # Validate and convert task_id string to ObjectId for MongoDB queries
        obj_id = ObjectId(task_id)
    except InvalidId:
        logger.error(f"Invalid task_id ObjectId string: {task_id}")
        return

    try:
        # Prepare HTTP request headers to simulate a real browser
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            )
        }

        # Delay to simulate human browsing behavior and reduce the chance of scraping blocks
        time.sleep(2)

        # Execute GET request to retrieve the product page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError on bad HTTP status

        # Parse the retrieved HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product details safely, raising ValueError if essential data is missing
        title_tag = soup.find("h1", class_="prod-ProductTitle")
        price_tag = soup.find("span", class_="price-characteristic")
        desc_tag = soup.find("div", class_="about-desc")

        if not title_tag or not price_tag:
            raise ValueError("Essential product information is missing from the page.")

        # Extract text content and build the product data dictionary
        product_data = {
            "url": url,
            "title": title_tag.get_text(strip=True),
            "price": price_tag.get_text(strip=True),
            "description": desc_tag.get_text(strip=True) if desc_tag else "",
            "scraped_at": datetime.utcnow()
        }

        # Insert the product data document into MongoDB 'products' collection
        try:
            db["products"].insert_one(product_data)
            logger.info(f"Inserted product data for URL: {url}")
        except Exception as insert_error:
            logger.error(f"MongoDB insert product error: {insert_error}")
            raise insert_error

        # Update the related scraping task document status to 'successful' with finish time
        try:
            db["tasks"].update_one(
                {"_id": obj_id},
                {"$set": {"status": "successful", "finished_at": datetime.utcnow().isoformat()}}
            )
            logger.info(f"Updated task {task_id} as successful")
        except Exception as update_error:
            logger.error(f"MongoDB update task success error: {update_error}")
            raise update_error

    except (RequestException, ValueError) as scrape_error:
        # Handle HTTP and value errors, mark task as 'failed' and log the error details
        logger.error(f"Scraping error for task {task_id}: {scrape_error}", exc_info=True)
        try:
            db["tasks"].update_one(
                {"_id": obj_id},
                {"$set": {
                    "status": "failed",
                    "finished_at": datetime.utcnow().isoformat(),
                    "error": str(scrape_error)
                }}
            )
            logger.info(f"Updated task {task_id} as failed due to scraping error")
        except Exception as mongo_error:
            logger.error(f"MongoDB update task failure error: {mongo_error}", exc_info=True)

    except Exception as unexpected_error:
        # Catch-all for any other unexpected exceptions, log and mark task failed
        logger.error(f"Unexpected error in scrape_product_task for task {task_id}: {unexpected_error}", exc_info=True)
        try:
            db["tasks"].update_one(
                {"_id": obj_id},
                {"$set": {
                    "status": "failed",
                    "finished_at": datetime.utcnow().isoformat(),
                    "error": str(unexpected_error)
                }}
            )
            logger.info(f"Updated task {task_id} as failed due to unexpected error")
        except Exception as mongo_error:
            logger.error(f"MongoDB update task failure error: {mongo_error}", exc_info=True)
