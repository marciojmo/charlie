import logging
import models
import time
import rabbitmq
import evolution
from config import settings

# Log settings
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def start_consumer() -> None:
    """
    Start consuming messages from RabbitMQ queue.
    Handles connection lifecycle and message processing.
    """
    connection_retry_time = int(settings.RABBITMQ_CONNECTION_RETRY_TIME)
    while True:
        try:
            with rabbitmq.get_rabbitmq_connection() as connection:
                channel = connection.channel()
                channel.queue_declare(
                    queue=settings.RABBITMQ_OUTGOING_MESSAGES_QUEUE, durable=True
                )

                logger.info(
                    f"[*] Listening on queue: {settings.RABBITMQ_OUTGOING_MESSAGES_QUEUE}"
                )

                # Process one message at a time
                channel.basic_qos(prefetch_count=1)
                channel.basic_consume(
                    queue=settings.RABBITMQ_OUTGOING_MESSAGES_QUEUE,
                    on_message_callback=process_message,
                    auto_ack=False,
                )
                channel.start_consuming()

        except KeyboardInterrupt:
            logger.info("Stopping consumer...")
            channel.stop_consuming()
            break
        except Exception as e:
            logger.error(f"Connection error: {e}", exc_info=True)
            logger.info(f"Retrying in {connection_retry_time} seconds...")
            time.sleep(connection_retry_time)


def process_message(channel, method, properties, body) -> None:
    """
    Process a message from RabbitMQ queue.

    Args:
        channel: RabbitMQ channel
        method: Delivery method
        properties: Message properties
        body: Message body
    """
    try:
        logger.info(f"[x] Received message: {body}")
        message = models.OutgoingMessage.model_validate_json(body.decode("utf-8"))
        evolution.send_whatsapp_message(message)
        channel.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"[!] Error processing message: {e}", exc_info=True)
        # Reject the message and requeue it
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


if __name__ == "__main__":
    start_consumer()
