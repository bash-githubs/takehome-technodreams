import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leads.settings")
app = Celery("leads")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
