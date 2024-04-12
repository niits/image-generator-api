from app.core.services.task_manager import TaskManageService
from app.settings import Settings
from functools import lru_cache
from fastapi import Depends
from celery import Celery
from kombu import Exchange, Queue


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_celery_app(settings: Settings = Depends(get_settings)):
    app = Celery(
        "celery",
        broker=str(settings.amqp_dsn),
        backend=str(settings.redis_dsn),
        result_extended=True,
    )

    app.conf.task_queues = [
        Queue(
            settings.queue_name,
            Exchange(settings.queue_name),
            routing_key=settings.queue_name,
        )
    ]

    return app


def get_task_manager(
    celery_app: Celery = Depends(get_celery_app),
    settings: Settings = Depends(get_settings),
) -> TaskManageService:
    return TaskManageService(celery_app, settings.queue_name, settings.task_name)
