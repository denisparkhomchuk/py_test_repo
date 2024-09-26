from dto.create_task_request import CreateTaskRequest
from todo_api import *


def test_task_creation():
    create_task_request = CreateTaskRequest(content="ABC", user_id="denisp", is_done=False)
    response = create_task(create_task_request)
    print(response)
    print(response.json())
