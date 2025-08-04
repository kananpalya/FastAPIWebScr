import os
from dotenv import load_dotenv

load_dotenv()  

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "fastapi_db")
TASKS_COLLECTION = os.getenv("TASKS_COLLECTION", "tasks")
