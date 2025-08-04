from fastapi import APIRouter, HTTPException, status, Body
from app.schemas.user_schema import UserCreate, UserResponse
from app.db import get_mongo_collection
from bson import ObjectId
from typing import List
from datetime import datetime

router = APIRouter()

collection = get_mongo_collection("users")

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate = Body(...)):
    existing = collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    user_doc = user.dict()
    user_doc["created_at"] = datetime.utcnow()
    result = collection.insert_one(user_doc)
    user_doc["_id"] = result.inserted_id
    return UserResponse(
        id=str(result.inserted_id),
        email=user.email,
        username=user.username,
        created_at=user_doc["created_at"]
    )

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(
        id=str(user["_id"]),
        email=user["email"],
        username=user["username"],
        created_at=user["created_at"]
    )
