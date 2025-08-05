readme_content =""" 
FastAPI Scraping Task Manager

A production-ready FastAPI application to manage scraping tasks with MongoDB, background processing, and user tracking.

Features:
1. User registration and management
2. Submit scraping tasks using product URLs
3. Background scraping with httpx + BeautifulSoup
4. Data storage in MongoDB (users, tasks, products)
5. Auto-generated interactive API docs via Swagger UI (/docs)
6. Modular project structure following best practices

Tech Stack:
- FastAPI – Web API framework
- MongoDB – NoSQL database
- httpx + BeautifulSoup – Asynchronous scraping
- Uvicorn – ASGI server
- Pydantic – Data validation
- Python 3.10+

Requirements:
- Python 3.10 or above
- MongoDB running locally at mongodb://localhost:27017
- Git

Setup Instructions:

1. Clone the Repository
   git clone https://github.com/kananpalya/FastAPIWebScr.git
   cd FastAPIWebScr

2. Set Up Virtual Environment

   Windows (Command Prompt / PowerShell):
   python -m venv env
   env\\Scripts\\activate

   macOS:
   python3 -m venv env
   source env/bin/activate

   Ubuntu / Linux:
   sudo apt update
   sudo apt install python3-venv -y
   python3 -m venv env
   source env/bin/activate

3. Install Dependencies
   pip install --upgrade pip
   pip install -r requirements.txt

4. Ensure MongoDB is Running

   Windows:
   Start MongoDB service via services.msc or run:
   net start MongoDB

   macOS / Ubuntu:
   If not running already:
   mongod --dbpath /your/mongodb/data/path

   If using Homebrew on macOS:
   brew services start mongodb-community@6.0

5. Start FastAPI Server
   uvicorn app.main:app --reload

   Once the server is running, open your browser and navigate to:
   http://127.0.0.1:8000/docs

   This will open the Swagger UI where you can interact with the API endpoints for:
   - Registering users
   - Creating scraping tasks
   - Viewing task and product data
"""