from pydantic import BaseModel


class TaskInfo(BaseModel):
    id: str
