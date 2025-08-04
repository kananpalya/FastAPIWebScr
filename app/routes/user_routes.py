from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserResponse
from app.db import get_db
import logging
from app.utils.exceptions import BadRequestException

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    """
    Create a new user in the database.

    Args:
        user (UserCreate): User data including username and email.

    Returns:
        UserResponse: User data including generated id.

    Raises:
        BadRequestException: If the provided data is invalid.
        HTTPException: If an error occurs while inserting the user.
    """
    db = get_db()
    # Basic validation example
    if not user.username or not user.email:
        raise BadRequestException(detail="Username and email must be provided.")
    try:
        new_user = user.dict()
        result = db["users"].insert_one(new_user)
        new_user["id"] = str(result.inserted_id)
        return UserResponse(**new_user)
    except BadRequestException:
        raise
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while creating user")
