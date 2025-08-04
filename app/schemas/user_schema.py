from pydantic import BaseModel, EmailStr
class UserCreate(BaseModel):
    """
    Schema for creating a new user.

    Attributes:
        username (str): The username of the user.
        email (EmailStr): The email address of the user.
    """
    username: str
    email: EmailStr

class UserResponse(UserCreate):
    """
    Schema for responding with user data including the assigned user ID.

    Attributes:
        id (str): Unique identifier for the user.
    """
    id: str
