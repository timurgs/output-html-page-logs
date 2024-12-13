import pika
from fastapi import APIRouter

from .models.models import Browse
from .settings import SETTINGS

router = APIRouter(prefix="/browse", tags=["Browse"])


@router.post("/")
async def browse_url(request: Browse):
    credentials = pika.PlainCredentials(
        f"{SETTINGS.RABBITMQ_DEFAULT_USER}",
        f"{SETTINGS.RABBITMQ_DEFAULT_PASS.get_secret_value()}"
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=f"{SETTINGS.RABBITMQ_HOST}",
            credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue='browse_queue')
    channel.basic_publish(exchange='', routing_key='browse_queue', body=request.url)
    connection.close()
    return {"message": "URL published to queue", "url": request.url}
