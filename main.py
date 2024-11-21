from fastapi import FastAPI


app = FastAPI()

tasks_data = [
    {"description": "Learn FastAPI", "priority": 2, "is_completed": False},
    {"description": "Do exercises", "priority": 1, "is_completed": True}
]

users_data = [
    {"username": "aaaa", "password": "bbbb", "is_admin": True},
    {"username": "qwe", "password": "alalal", "is_admin": False}
]


@app.get("/")
def root():
    return {"message": "Hello world!!!"}


@app.get("/tasks")
def get_tasks():
    return {"result": tasks_data}


@app.get("/users")
def get_users():
    return {"result": users_data}
