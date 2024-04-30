
from pydantic import BaseModel


class WebhookPayload(BaseModel):
    id: int
    tenantId: int
    channel: str
    source: str
    started: str
    ended: str
