import uuid
import datetime
from pydantic import BaseModel, Field, HttpUrl


class Link(BaseModel):
    id: uuid.UUID
    redirect_url: HttpUrl
    is_active: bool
    created_at: datetime.datetime

    class Config:
        from_attributes = True
        orm_mode = True


class LinkPayload(BaseModel):
    redirect_url: HttpUrl