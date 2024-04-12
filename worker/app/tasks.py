import time

from .worker import app, settings


@app.task(name=settings.task_name, bind=True)
def task(self, prompt: str, negative_prompt: str):
    time.sleep(5)
    return {
        "s3_path": None,
        "message": "Not implemented yet.",
    }
