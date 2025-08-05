import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Configuration settings for the application.

    Attributes:
        MONGO_URL (str): MongoDB connection URI, loaded from the environment variable 'MONGO_URI'.
                         Defaults to 'mongodb://localhost:27017' if not set.
        MONGO_DB (str): Name of the MongoDB database to use, loaded from the environment variable 'DB_NAME'.
                        Defaults to 'projfastapi' if not set.
    """

    MONGO_URL: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("DB_NAME", "projfastapi")

settings = Settings()
