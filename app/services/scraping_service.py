# # File: app/services/scraping_service.py

# import requests
# from bs4 import BeautifulSoup
# import time
# from datetime import datetime
# from app.db import get_db
# import logging
# from bson.objectid import ObjectId
# from bson.errors import InvalidId
# from requests.exceptions import RequestException

# logger = logging.getLogger(__name__)

# def scrape_product_task(task_id: str, url: str) -> None:
#     db = get_db()
#     try:
#         obj_id = ObjectId(task_id)
#     except InvalidId:
#         logger.error(f"Invalid task_id: {task_id}")
#         return

#     try:
#         headers = {
#             "User-Agent": (
#                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
#             )
#         }

#         time.sleep(2)
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, "html.parser")

#         # Try to get product title or fallback to page title or URL
#         title_tag = soup.find("h1", class_="prod-ProductTitle")
#         if title_tag and title_tag.get_text(strip=True):
#             title = title_tag.get_text(strip=True)
#         else:
#             # fallback: HTML page <title> tag or URL as last resort
#             title = soup.title.string.strip() if soup.title else url

#         # Try to get product price or fallback to unknown
#         price_whole_tag = soup.find("span", class_="price-characteristic")
#         price_fraction_tag = soup.find("span", class_="price-mantissa")
#         if price_whole_tag and price_fraction_tag:
#             price = f"{price_whole_tag.get('content', '').strip()}.{price_fraction_tag.get('content', '').strip()}"
#         else:
#             price_tag = soup.find("span", class_="price-group")
#             price = price_tag.get_text(strip=True) if price_tag else "Price not found"

#         # Try to get description or fallback to empty
#         desc_tag = soup.find("div", class_="about-desc")
#         description = desc_tag.get_text(strip=True) if desc_tag else ""

#         product_data = {
#             "url": url,
#             "title": title,
#             "price": price,
#             "description": description,
#             "scraped_at": datetime.utcnow(),
#             "note": "Partial data scraped: fallback used where necessary"
#         }

#         db["products"].insert_one(product_data)
#         db["tasks"].update_one(
#             {"_id": obj_id},
#             {"$set": {"status": "successful", "finished_at": datetime.utcnow().isoformat()}}
#         )
#         logger.info(f"Scraping successful for task {task_id} with partial/fallback data.")

#     except (RequestException, Exception) as scrape_error:
#         logger.error(f"Scraping error for task {task_id}: {scrape_error}", exc_info=True)
#         try:
#             db["tasks"].update_one(
#                 {"_id": obj_id},
#                 {
#                     "$set": {
#                         "status": "failed",
#                         "finished_at": datetime.utcnow().isoformat(),
#                         "error": str(scrape_error)
#                     }
#                 }
#             )
#         except Exception as mongo_err:
#             logger.error(f"Update task failure error: {mongo_err}", exc_info=True)











# # File: app/services/scraping_service.py

# import requests
# from bs4 import BeautifulSoup
# import random
# import time
# from datetime import datetime
# from app.db import get_db
# import logging
# from bson.objectid import ObjectId
# from bson.errors import InvalidId

# logger = logging.getLogger(__name__)

# USER_AGENTS = [
#     # A few real browser agents for realism
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.119 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1"
# ]

# def scrape_product_task(task_id: str, url: str) -> None:
#     db = get_db()
#     try:
#         obj_id = ObjectId(task_id)
#     except InvalidId:
#         logger.error(f"Invalid task_id: {task_id}")
#         return

#     for attempt in range(3):  # Try a couple of times with random user-agents and delays
#         try:
#             headers = {
#                 "User-Agent": random.choice(USER_AGENTS),
#                 "Accept-Language": "en-US,en;q=0.9",
#                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#                 "Referer": "https://www.google.com/"
#             }

#             sleep_time = random.randint(3, 8)  # random delay (could adjust this)
#             time.sleep(sleep_time)

#             response = requests.get(url, headers=headers, timeout=20)
#             response.raise_for_status()

#             soup = BeautifulSoup(response.text, "html.parser")

#             # Always extract the HTML <title> for reference
#             page_title = soup.title.string.strip() if soup.title else "No HTML <title> found"

#             # Try product title
#             title_tag = soup.find("h1", class_="prod-ProductTitle")
#             if title_tag and title_tag.get_text(strip=True):
#                 product_title = title_tag.get_text(strip=True)
#             else:
#                 product_title = page_title

#             # Try product price
#             price_whole_tag = soup.find("span", class_="price-characteristic")
#             price_fraction_tag = soup.find("span", class_="price-mantissa")
#             if price_whole_tag and price_fraction_tag:
#                 price = f"{price_whole_tag.get('content', '').strip()}.{price_fraction_tag.get('content', '').strip()}"
#             else:
#                 price_tag = soup.find("span", class_="price-group")
#                 if price_tag and price_tag.get_text(strip=True):
#                     price = price_tag.get_text(strip=True)
#                 else:
#                     price = "Price not found"

#             # Try description
#             desc_tag = soup.find("div", class_="about-desc")
#             description = desc_tag.get_text(strip=True) if desc_tag else ""

#             product_data = {
#                 "url": url,
#                 "title": product_title,
#                 "raw_html_title": page_title,
#                 "price": price,
#                 "description": description,
#                 "scraped_at": datetime.utcnow(),
#                 "note": (
#                     f"Scraping attempt {attempt+1}. If data is partial, Walmart likely returned a bot/captcha page. "
#                     "Advanced anti-bot techniques required for full data."
#                 )
#             }

#             db["products"].insert_one(product_data)
#             db["tasks"].update_one(
#                 {"_id": obj_id},
#                 {
#                     "$set": {
#                         "status": "successful",
#                         "finished_at": datetime.utcnow().isoformat(),
#                         "note": f"Scraping completed with attempt {attempt+1}"
#                     }
#                 }
#             )
#             logger.info(f"Scraping attempt {attempt+1} for task {task_id}. Title: {product_title!r}, Price: {price!r}")
#             return  # Success, exit

#         except Exception as scrape_error:
#             logger.error(f"Scraping error (attempt {attempt+1}) for task {task_id}: {scrape_error}", exc_info=True)
#             time.sleep(2)

#     # If none of the attempts worked, log failure
#     try:
#         db["tasks"].update_one(
#             {"_id": obj_id},
#             {
#                 "$set": {
#                     "status": "failed",
#                     "finished_at": datetime.utcnow().isoformat(),
#                     "error": "All attempts returned partial or no data. Advanced scraping required for Walmart."
#                 }
#             }
#         )
#     except Exception as mongo_err:
#         logger.error(f"Update task failure error: {mongo_err}", exc_info=True)










# File: app/services/scraping_service.py

import requests
from bs4 import BeautifulSoup
import re
import random
import time
from datetime import datetime
from app.db import get_db
import logging
from bson.objectid import ObjectId
from bson.errors import InvalidId


logger = logging.getLogger(__name__)


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.119 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1"
]


def extract_price(soup):
    """
    Extract the product price from the BeautifulSoup object using multiple Walmart-specific selectors
    and fallbacks. Returns price as a string if found, otherwise empty string.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the product page.

    Returns:
        str: Price string including currency symbols if found, else empty string.
    """
    price_whole = soup.find("span", class_="price-characteristic")
    price_frac = soup.find("span", class_="price-mantissa")
    if price_whole and price_frac:
        return f"{price_whole.get('content','').strip()}.{price_frac.get('content','').strip()}"
    price_group = soup.find("span", class_="price-group")
    if price_group and price_group.get_text(strip=True):
        return price_group.get_text(strip=True)
    price_regex = re.search(r'[\$\₹]\s*\d+[,\.]?\d*', soup.text)
    if price_regex:
        return price_regex.group().strip()
    return ""


def extract_description(soup):
    """
    Extract the product description from the BeautifulSoup object using common Walmart selectors
    and fallbacks including meta tags and nearby content sections.

    Args:
        soup (BeautifulSoup): Parsed HTML content of the product page.

    Returns:
        str: Description text if found, otherwise empty string.
    """
    desc_div = soup.find("div", class_="about-desc")
    if desc_div and desc_div.get_text(strip=True):
        return desc_div.get_text(strip=True)
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content", "").strip():
        return meta_desc.get("content", "").strip()
    bullets = soup.find("ul", class_="about-desc-list")
    if bullets:
        items = [li.get_text(strip=True) for li in bullets.find_all("li")]
        if items:
            return " | ".join(items)
    for h in soup.find_all(['h2','h3']):
        if 'product details' in h.get_text(strip=True).lower():
            sib = h.find_next('div')
            if sib and sib.get_text(strip=True):
                return sib.get_text(strip=True)
    return ""


def scrape_product_task(task_id: str, url: str) -> None:
    """
    Background scraping task to extract product details from a Walmart product page URL
    and insert data into MongoDB. It attempts multiple times with random user-agents
    and delays to reduce detection risk. Updates the task status in the database 
    accordingly.

    Args:
        task_id (str): The MongoDB task document ID as a string.
        url (str): The Walmart product page URL to scrape.

    Returns:
        None
    """
    db = get_db()
    try:
        obj_id = ObjectId(task_id)
    except InvalidId:
        logger.error(f"Invalid task_id: {task_id}")
        return

    for attempt in range(3):
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Accept-Language": "en-US,en;q=0.9",
            }
            time.sleep(random.randint(2, 6))
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract page title or fallback to url
            page_title = soup.title.string.strip() if soup.title else ""
            prod_title = ""
            title_tag = soup.find("h1", class_="prod-ProductTitle")
            if title_tag and title_tag.get_text(strip=True):
                prod_title = title_tag.get_text(strip=True)
            else:
                prod_title = page_title if page_title else url

            price = extract_price(soup)
            description = extract_description(soup)

            product_data = {
                "url": url,
                "title": prod_title,
                "raw_html_title": page_title,
                "price": price,
                "description": description,
                "scraped_at": datetime.utcnow()
            }

            db["products"].insert_one(product_data)
            db["tasks"].update_one(
                {"_id": obj_id},
                {
                    "$set": {
                        "status": "successful",
                        "finished_at": datetime.utcnow().isoformat()
                    }
                }
            )
            logger.info(f"Scraping attempt {attempt+1} for task {task_id}. Title: {prod_title!r}, Price: {price!r}")
            return

        except Exception as scrape_error:
            logger.error(f"Scraping error (attempt {attempt+1}) for task {task_id}: {scrape_error}", exc_info=True)
            time.sleep(1)

    try:
        db["tasks"].update_one(
            {"_id": obj_id},
            {
                "$set": {
                    "status": "failed",
                    "finished_at": datetime.utcnow().isoformat(),
                    "error": "All attempts could not extract product data. Walmart may block bots."
                }
            }
        )
    except Exception as mongo_err:
        logger.error(f"Update task failure error: {mongo_err}", exc_info=True)
#new pr