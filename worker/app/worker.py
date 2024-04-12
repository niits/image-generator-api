from celery import Celery
from kombu import Exchange, Queue
from .settings import Settings

settings = Settings()

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
