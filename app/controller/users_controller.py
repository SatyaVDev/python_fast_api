from app.services import UserService

user_service = UserService()

def get_all_users(user_id :int) :
        return user_service.get_user(user_id)




