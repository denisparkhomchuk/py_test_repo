from fastapi import FastAPI
from fastapi_course.task_2_2.models import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.get("/user")
def get_user():
    user = User(name="John Doe", id=1, age=2)
    return user

@app.post("/user")
def post_user(user: User):
    is_adult = user.age >= 18
    user.is_adult = is_adult
    print(user)
    return user