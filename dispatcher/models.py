import pydantic
from typing import List, Optional


class IncomingMessage(pydantic.BaseModel):
    username: str
    number: str
    text: str
    is_group: bool | None
    mentioner: str | None

    def __str__(self):
        return f"[IncomingMessage] Name: {self.username}. Number: {self.number}. Text: {self.text}."


class OutgoingMessage(pydantic.BaseModel):
    number: str
    text: str
    mentioned: Optional[List[str]] | None

    def __str__(self):
        return f"[Outgoing Message] Number: {self.number}. Text: {self.text}"
