import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Word.settings')

app =Celery('Word')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')