from fastapi import APIRouter, HTTPException, Request

from app.controller import users_controller

router = APIRouter()


@router.get("/users")
def get_users(request: Request, user_id: int):
    try:
        db = request.app.state.mongo_db

        return users_controller.get_all_users(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"User with ID {user_id}"}
