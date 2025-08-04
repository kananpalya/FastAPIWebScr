from pydantic import BaseModel, Field
class UserModel(BaseModel):
    """
    User database model schema for MongoDB documents.

    Attributes:
        id (str): The unique identifier of the user (MongoDB ObjectId as string, aliased as "_id").
        username (str): The username of the user.
        email (str): The user's email address.
    """
    id: str = Field(default_factory=str, alias="_id")
    username: str
    email: str

    class Config:
        """
        Pydantic configuration for ORM compatibility and alias support.
        """
        orm_mode = True
        allow_population_by_field_name = True
