from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.post("/calculate")
async def root(num1:int, num2:int):
    result = num1 + num2
    return {"result": result}