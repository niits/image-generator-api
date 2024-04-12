from pydantic import BaseModel


class TaskInput(BaseModel):
    prompt: str
    negative_prompt: str
