from fastapi import FastAPI, Depends, HTTPException, status
from app.core.services.task_manager import TaskManageService
from app.core.entities import TaskInput, TaskInfo, TaskResult
from app.dependencies import get_task_manager

import logging

app = FastAPI()


@app.post("/send_task", response_model=TaskInfo, status_code=status.HTTP_201_CREATED)
def send_task(
    data: TaskInput, task_manager: TaskManageService = Depends(get_task_manager)
):
    try:
        task_id = task_manager.send_task(data)
    except Exception as e:
        logging.critical(f"Error sending task: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service Unavailable",
        )
    return TaskInfo(id=task_id)


@app.get("/get_task", status_code=status.HTTP_200_OK)
def get_task(task_id: str, task_manager: TaskManageService = Depends(get_task_manager)):
    async_result = task_manager.get_task(task_id)

    if async_result.args is None or len(async_result.args) != 2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Can not find task with id {task_id}",
        )

    prompt, negative_prompt = async_result.args
    return TaskResult(
        status=async_result.status,
        result=async_result.result,
        task_input=TaskInput(prompt=prompt, negative_prompt=negative_prompt),
    )
