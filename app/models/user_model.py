from app.db.mongo import db

from app.schemas.user_schema import UserSchema
from bson import ObjectId

user_collection = db["users"]


async def create_user(user_data: dict) -> UserSchema:
    result = await user_collection.insert_one(user_data)
    user_data["_id"] = result.inserted_id
    return user_data
