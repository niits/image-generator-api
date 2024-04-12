from pydantic import BaseModel
from typing import Literal, Optional
from app.core.entities.task_input import TaskInput


class Result(BaseModel):
    s3_path: Optional[str]
    message: str


class TaskResult(BaseModel):
    status: Literal[
        "PENDING",
        "RECEIVED",
        "STARTED",
        "SUCCESS",
        "FAILURE",
        "REVOKED",
        "RETRY",
        "IGNORED",
    ]
    result: Optional[Result]

    task_input: Optional[TaskInput]
