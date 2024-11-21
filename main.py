from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Response
from fastapi.responses import JSONResponse


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


def get_item_index_by_id(items_list, id_):
    for i, item in enumerate(items_list):
        if item["id"] == id_:
            return i


@app.get("/")
def root():
    return {"message": "Hello world!!!"}


@app.get("/tasks")
def get_tasks():
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"result": tasks_data})


@app.get("/users")
def get_users():
    return {"result": users_data}


@app.get("/tasks/{id_}")
def get_single_task(id_: int):
    target_task = get_item_by_id(tasks_data, id_)

    if target_task is None:
        message = {"error": f"Task with id={id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_task}


@app.get("/users/{id_}")
def get_single_user(id_: int):
    target_user = get_item_by_id(users_data, id_)

    if target_user is None:
        message = {"error": f"User with id={id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_user}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
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


@app.delete("/tasks/{id_}")
def delete_task(id_: int):
    target_index = get_item_index_by_id(tasks_data, id_)

    if target_index is None:
        message = {"error": f"Task with id {id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    tasks_data.pop(target_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/tasks/{id_}")
def update_task(id_: int, body: TaskBody):
    task_data = body.model_dump()
    target_index = get_item_index_by_id(tasks_data, id_)
    if target_index is None:
        message = {"error": f"Task with id {id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    task_data["id"] = id_

    tasks_data[target_index] = task_data
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": f"Task {id_} updated", "details": task_data})
