from pymongo import MongoClient
import sys
import os

# Ensure the parent directory is in sys.path to help with module resolution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import settings

client = MongoClient(settings.MONGO_URL)
db = client[settings.MONGO_DB]
"""
MongoDB client and database instance initialized using connection settings.

- `client`: MongoClient connected to the MongoDB server specified in settings.
- `db`: Reference to the MongoDB database named as per settings.MONGO_DB.
"""

def get_db():
    """
    Retrieve the MongoDB database instance.

    Returns:
        Database: The MongoDB database object for performing queries.
    """
    return db
