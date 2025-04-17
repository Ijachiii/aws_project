# core/tasks.py

import time
import logging
from celery import shared_task
from .models import Process

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def process_message(self, message_id):
    try:
        instance = Process.objects.get(id=message_id)
        instance.status = 'processing'
        instance.save()

        # Simulate time-consuming work
        time.sleep(15)

        # Dummy result
        result = f"Processed message from {instance.email}"

        instance.status = 'completed'
        instance.result = result
        instance.save()
        logger.info(result)
        return result
    except Exception as e:
        instance.status = 'failed'
        instance.result = str(e)
        instance.save()
        raise self.retry(exc=e, countdown=5, max_retries=3)