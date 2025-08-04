import requests
from bs4 import BeautifulSoup

def scrape_product_data(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Example extraction: title and price
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "No title found"

    price_tag = soup.find("span", {"class": "price-characteristic"})
    price = price_tag.text.strip() if price_tag else "Price not found"

    return {
        "title": title,
        "price": price,
        "url": url
    }
