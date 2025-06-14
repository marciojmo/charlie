import os
from dotenv import load_dotenv


class Settings:
    """Application configuration settings."""

    def __init__(self):
        load_dotenv()
        self.EVOLUTION_SERVICE_ENDPOINT = os.getenv("EVOLUTION_SERVICE_ENDPOINT")
        self.INSTANCE_NAME = os.getenv("INSTANCE_NAME")
        self.API_KEY = os.getenv("API_KEY")
        self.RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
        self.RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
        self.RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
        self.RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
        self.RABBITMQ_OUTGOING_MESSAGES_QUEUE = os.getenv(
            "RABBITMQ_OUTGOING_MESSAGES_QUEUE", "outgoing_messages"
        )
        self.RABBITMQ_CONNECTION_RETRY_TIME = os.getenv(
            "RABBITMQ_CONNECTION_RETRY_TIME", "5"
        )


# Global configuration instance
settings = Settings()
