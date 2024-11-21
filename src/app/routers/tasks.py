from fastapi import HTTPException, status, Response, APIRouter
from fastapi.responses import JSONResponse

from app.models import TaskBody
from app.utils import get_item_by_id, get_item_index_by_id


tasks_data = [
    {"id": 1, "description": "Learn FastAPI", "priority": 2, "is_completed": False},
    {"id": 2, "description": "Do exercises", "priority": 1, "is_completed": True}
]

router = APIRouter()


@router.get("/tasks")
def get_tasks():
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"result": tasks_data})

@router.get("/tasks/{id_}")
def get_single_task(id_: int):
    target_task = get_item_by_id(tasks_data, id_)

    if target_task is None:
        message = {"error": f"Task with id={id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"result": target_task}



@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskBody):
    new_task = body.model_dump()
    new_task["id"] = len(tasks_data) + 1

    tasks_data.append(new_task)

    return {"message": "New task added", "details": new_task}


@router.delete("/tasks/{id_}")
def delete_task(id_: int):
    target_index = get_item_index_by_id(tasks_data, id_)

    if target_index is None:
        message = {"error": f"Task with id {id_} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    tasks_data.pop(target_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/tasks/{id_}")
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
