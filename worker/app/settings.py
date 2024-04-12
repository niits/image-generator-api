from pydantic import AmqpDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    task_name: str
    queue_name: str
    amqp_dsn: AmqpDsn
    redis_dsn: RedisDsn