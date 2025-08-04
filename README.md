# FastAPI Scraping Task Manager

A simple FastAPI app to manage background scraping tasks and MongoDB integration.

## ✅ Features

- Create users
- Submit scraping tasks with URLs
- Background scraping using httpx + BeautifulSoup
- MongoDB for persistence (users, tasks)
- FastAPI docs

## 🛠 Requirements

- Python 3.10+
- MongoDB running locally on `mongodb://localhost:27017`

## 🚀 Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
