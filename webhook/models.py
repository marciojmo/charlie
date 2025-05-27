import pydantic
from typing import Optional


class EvolutionData(pydantic.BaseModel):
    pushName: str
    key: dict
    message: dict
    contextInfo: Optional[dict] = pydantic.Field(default_factory=dict)


class IncomingMessage(pydantic.BaseModel):
    username: str
    number: str
    text: str
    is_group: bool | None
    mentioner: str | None

    def __str__(self):
        return f"[IncomingMessage] Name: {self.username}. Number: {self.number}. Text: {self.text}."
