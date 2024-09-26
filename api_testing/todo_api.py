import requests
from dto.create_task_request import CreateTaskRequest
import json

ENDPOINT = "https://todo.pixegami.io"

def create_task(request: CreateTaskRequest):
    payload = request.model_dump()
    print(payload)
    response = requests.put(f'{ENDPOINT}/create-task', json=payload)
    return response

