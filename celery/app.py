import os
from celery import Celery

# os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')
# app = Celery('app')
# app.config_from_envvar('CELERY_CONFIG_MODULE')

app = Celery('tasks')#, backend='rpc://', broker='pyamqp://')
# app = Celery('tasks', broker='redis://redis:6379/0')
# app.config_from_object('celery_config', namespace="CELERY")

@app.task
def add(x, y):
    return x + y