from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def root():
    file = open("fastapi_course/task_2_1/index.html", "r")
    content = file.read()
    print(content)
    file.close()
    return HTMLResponse(content=content, status_code=200)