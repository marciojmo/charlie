import logging
import requests
from config import settings
from models import OutgoingMessage

logger = logging.getLogger(__name__)


def send_whatsapp_message(message: OutgoingMessage):
    url = f"{settings.EVOLUTION_SERVICE_ENDPOINT}/message/sendText/{settings.INSTANCE_NAME}"
    headers = {"Content-Type": "application/json", "apikey": settings.API_KEY}

    logger.info(f"[*] Sending message to evolution instance {url}")
    response = requests.post(
        url, json=message.model_dump(exclude_none=True), headers=headers, timeout=30
    )
    response.raise_for_status()
    logger.info("[x] Message successfully sent!")
