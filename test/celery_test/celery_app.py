from celery import Celery

redis_config='redis://127.0.0.1:6379/0'
celery_app = Celery(__name__, backend=redis_config, broker=redis_config)


@celery_app.task
def async_add(x, y):
    return x + y
