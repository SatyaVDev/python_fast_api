from app.services import UserService

user_service = UserService()


async def get_all_users(db, user_id: int):
    users_collection = db["users"]  # 👈 Access collection
    users_cursor = users_collection.find({})
    users = await users_cursor.to_list(length=100)  # Adjust limit as needed
    # print(users, "-----------")
    return users
