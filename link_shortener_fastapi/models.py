import uuid
import datetime
from typing_extensions import Annotated
from pydantic import BaseModel, AfterValidator, Field, HttpUrl


# Using annotatedValidator to validate redirect_url and return str
HttpUrlString = Annotated[HttpUrl, AfterValidator(lambda v: str(v))]

class Link(BaseModel):
    id: uuid.UUID
    redirect_url: str
    is_active: bool
    created_at: datetime.datetime

    class Config:
        from_attributes = True


class LinkPayload(BaseModel):
    redirect_url: HttpUrlString