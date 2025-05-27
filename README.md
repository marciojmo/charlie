# Charlie - A microserviced WhatsApp Bot with Intent Classification

Charlie is a sophisticated WhatsApp bot built on top of the Evolution API, featuring a microservices architecture with RabbitMQ for message handling and a custom intent classification system.

## What it Does?

Charlie can detect user intent and reply in one of the following categories (Brazilian Portuguese):
- Reply with a biblical verse.
- Reply with the fortune of the day.
- Reply with a gym motivation.

It uses a simple hand-trained intent classifier. The notebook is available in this repository under the intent-parser/pretrained_models folder.


## Architecture

The system consists of several microservices:

- **Evolution API**: Handles WhatsApp connection and messaging.
- **Webhook Service**: Receives incoming messages from the Evolution API.
- **Intent Parser**: Processes messages and classifies intents
  - **Intent Classifier**: A simple classifier for detecting user intent based on text similarity.
- **Dispatcher Service**: Dispatches messages back to the Evolution API
- **RabbitMQ**: Message broker for inter-service communication
- **PostgreSQL**: Database for persistent storage
- **Redis**: Caching layer

### Service Communication Flow

1. Messages arrive at Evolution API.
2. Webhook service receives messages, converts into a known format and publishes it into `incoming_messages` queue on RabbitMQ.
3. Intent Parser consumes messages from the `incoming_messages` queue, classifies the user intent, process and publishes back the result into the `outgoing_messages` queue on RabbitMQ.
4. Dispatcher consumes the `outgoing_messages` queue on RabbitMQ and invoke the Evolution API to send the message to Whatsapp.

## Prerequisites

- Docker and Docker Compose
- Python 3.9+ (for local development)

This project uses UV for python package management. Check it out at [UV on Github](https://github.com/astral-sh/uv).


## Running with Docker

1. Start all services by running:
```bash
docker-compose up -d
```

2. Access the evolution API management at:
http://localhost:8080/manager

3. Connect your bot number by clicking the `Instance +` button and following the instructions.

4. Under `Events > Webhook`, enable the webhook and set the URL to `http://host.docker.internal:8000/webhook`

5. Under `Events > Webhook`, set the `MESSAGES_UPSERT` event to enabled.

36. Check services status and view logs
```bash
docker ps
docker-compose logs -f [service-name]
```

## Service Details

### Evolution API
- Port: 8080
- Handles WhatsApp connection
- Manages message sending/receiving

### Webhook Service
- Port: 8000
- Receives incoming messages and parses them into a known format.
- Publishes to RabbitMQ queue: `incoming_messages`
- Python FastAPI application

### Intent Parser
- Processes messages for intent classification
- Uses hand-trained classification model
- Publishes to RabbitMQ queue: `outgoing_messages`
- Python service with scikit-learn

### Dispatcher
- Communicates with Evolution API for responses
- Python service

### RabbitMQ
- Management Interface: http://localhost:15672
- Queues:
  - incoming_messages
  - outgoing_messages

### PostgreSQL
- Port: 5432
- Database: evolution
- User: charlie

### Redis
- Port: 6379
- Used for caching and session management

## Development Guidelines

### Code Style
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions and classes

### Testing
There are no tests. Would you like to contribute?

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

Copyright (c) 2025 Microserviced Whatspp Bot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.