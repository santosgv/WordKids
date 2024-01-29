import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Word.settings')

app =Celery('Word')
app.conf.enable_utc= False
app.conf.update(timezone ='America/Sao_Paulo')

app.config_from_object('django.conf.settings',namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')