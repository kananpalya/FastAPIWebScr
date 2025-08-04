from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fastapinew"]

def get_mongo_collection(name: str):
    return db[name]
