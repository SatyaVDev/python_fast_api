from fastapi import APIRouter, HTTPException

from app.controller import users_controller

router = APIRouter()


@router.get("/users")
def get_users(user_id : int):
    try:
        return users_controller.get_all_users(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"User with ID {user_id}"}
