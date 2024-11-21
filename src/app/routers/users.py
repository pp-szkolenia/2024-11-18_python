from fastapi import HTTPException, status, APIRouter

from app.models import UserBody
from app.utils import get_item_by_id, get_item_index_by_id


users_data = [
    {"id": 1, "username": "aaaa", "password": "bbbb", "is_admin": True},
    {"id": 2, "username": "qwe", "password": "alalal", "is_admin": False}
]

router = APIRouter()


@router.get("/users")
def get_users():
    print("test")
    return {"result": users_data}


@router.get("/users/{id_}")
def get_single_user(id_: int):
    target_user = get_item_by_id(users_data, id_)

    if target_user is None:
        message = {"error": f"User with id={id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_user}


@router.post("/users")
def create_user(body: UserBody):
    new_user = body.model_dump()
    new_user["id"] = len(users_data) + 1

    users_data.append(new_user)

    return {"message": "New user added", "details": new_user}


