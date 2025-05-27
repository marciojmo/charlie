import logging
import fastapi
import models
import rabbitmq
from config import settings

# Log settings
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# FastAPI
app = fastapi.FastAPI(
    title="Whatsapp Bot - Evolution Webhook",
    description="A webhook service for processing WhatsApp messages from evolution.",
    version="1.0.0",
)


@app.post("/webhook", status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def evolution_webhook(request: fastapi.Request) -> None:
    """Handle incoming webhook requests.

    Args:
        request (Request): The request object.

    Returns:
        None

    Raises:
        HTTPException: If the request is invalid or processing fails.
    """
    try:
        body = await request.json()
        data = body.get("data", {})

        if not data:
            raise fastapi.HTTPException(
                status_code=400, detail="Invalid request: missing data"
            )

        webhook_data = models.EvolutionData(**data)

        # Extract message details
        username = webhook_data.pushName
        remote_jid = webhook_data.key.get("remoteJid")

        if not remote_jid:
            raise fastapi.HTTPException(
                status_code=400, detail="Invalid request: missing remoteJid"
            )

        number, domain = remote_jid.split("@")
        is_group = domain == "g.us"
        text = webhook_data.message.get("conversation", "").strip()
        mentioner = webhook_data.contextInfo.get("mentionedJid", [None])[0]

        message = models.IncomingMessage(
            username=username,
            number=number,
            text=text,
            is_group=is_group,
            mentioner=mentioner,
        )

        logger.info(f"Enqueuing new message: {message}")
        rabbitmq.publish_message(settings.RABBITMQ_INCOMING_MESSAGES_QUEUE, message)

    except ValueError as e:
        logger.error(f"Invalid request data: {e}")
        raise fastapi.HTTPException(status_code=400, detail="Invalid request data")
    except Exception as e:
        logger.error(f"Unexpected error processing webhook: {e}")
        raise fastapi.HTTPException(status_code=500, detail="Internal server error")
