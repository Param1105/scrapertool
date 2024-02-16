import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapertool.settings')

app = Celery('scrapertool')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
        'every-day-at-midnight':{
        'task':'scraper.tasks.fetch_records',
        'schedule':crontab(minute=0, hour=0),            # Execute daily at midnight
        # 'schedule':crontab(minute='*/5'),            # Execute every 5 mins
    }
}