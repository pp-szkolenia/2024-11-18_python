from fastapi import FastAPI


app = FastAPI()

tasks_data = [
    {"description": "Learn FastAPI", "priority": 2, "is_completed": False},
    {"description": "Do exercises", "priority": 1, "is_completed": True}
]


@app.get("/")
def root():
    return {"message": "Hello world!!!"}


@app.get("/tasks")
def get_tasks():
    return {"result": tasks_data}
