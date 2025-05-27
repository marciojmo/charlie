import logging
import pika
from contextlib import contextmanager
from config import settings


logger = logging.getLogger(__name__)


@contextmanager
def get_rabbitmq_connection():
    """Context manager for RabbitMQ connection.

    Yields:
        pika.BlockingConnection: RabbitMQ connection

    Raises:
        MessageQueueConnectionError: If connection fails
    """
    connection = None
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=pika.PlainCredentials(
                    settings.RABBITMQ_USER, settings.RABBITMQ_PASS
                ),
                heartbeat=600,
                blocked_connection_timeout=300,
            )
        )
        yield connection
    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Failed to connect to RabbitMQ: {e}")
        raise
    finally:
        if connection and connection.is_open:
            connection.close()


def publish_message(queue_id: str, message) -> None:
    """Publishes a message into a rabbitmq queue.

    Args:
        queue_id (str): The target queue identifier.
        message: The message to be published (must have model_dump_json method).

    Raises:
        MessageQueuePublishError: If message publishing fails.
    """
    try:
        with get_rabbitmq_connection() as connection:
            channel = connection.channel()
            channel.queue_declare(queue=queue_id, durable=True)

            channel.basic_publish(
                exchange="",
                routing_key=queue_id,
                body=message.model_dump_json().encode("utf-8"),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ),
            )

            logger.info(f"Published message to '{queue_id}': {message}")
    except Exception as e:
        logger.error(f"Failed to publish message: {e}")
        raise
