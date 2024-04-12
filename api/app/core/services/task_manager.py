from celery import Celery
from uuid import uuid4

from app.core.entities.task_input import TaskInput


class TaskManageService:
    def __init__(self, client: Celery, queue_name: str, task_name: str):
        self.client = client
        self.queue_name = queue_name
        self.task_name = task_name

    def send_task(self, task_input: TaskInput) -> str:
        task_id = str(uuid4())
        self.client.send_task(
            self.task_name,
            args=[task_input.prompt, task_input.negative_prompt],
            queue=self.queue_name,
            task_id=task_id,
        )
        return task_id

    def get_task(self, task_id):
        return self.client.AsyncResult(task_id)
