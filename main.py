from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()


class TaskBody(BaseModel):
    description: str
    priority: int | None = None
    is_completed: bool = False


class UserBody(BaseModel):
    username: str
    password: str
    is_admin: bool = False


tasks_data = [
    {"id": 1, "description": "Learn FastAPI", "priority": 2, "is_completed": False},
    {"id": 2, "description": "Do exercises", "priority": 1, "is_completed": True}
]

users_data = [
    {"id": 1, "username": "aaaa", "password": "bbbb", "is_admin": True},
    {"id": 2, "username": "qwe", "password": "alalal", "is_admin": False}
]


def get_item_by_id(items_list, id_):
    for item in items_list:
        if item["id"] == id_:
            return item
    return None


@app.get("/")
def root():
    return {"message": "Hello world!!!"}


@app.get("/tasks")
def get_tasks():
    return {"result": tasks_data}


@app.get("/users")
def get_users():
    return {"result": users_data}


@app.get("/users/{id_}")
def get_single_user(id_: int):
    target_user = get_item_by_id(users_data, id_)
    return {"result": target_user}


@app.post("/tasks")
def create_task(body: TaskBody):
    new_task = body.model_dump()
    new_task["id"] = len(tasks_data) + 1

    tasks_data.append(new_task)

    return {"message": "New task added", "details": new_task}


@app.post("/users")
def create_user(body: UserBody):
    new_user = body.model_dump()
    new_user["id"] = len(users_data) + 1

    users_data.append(new_user)

    return {"message": "New user added", "details": new_user}
