# app/services/user_service.py

class UserService:
    def __init__(self):
        # Pretend we have a user database or repo here
        self._users = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"},
        }

    def get_user(self, user_id: int):
        user = self._users.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def list_users(self):
        return list(self._users.values())
