import uuid
import datetime
from sqlalchemy import Column, ForeignKey, Table, orm, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID


class Base(orm.DeclarativeBase):
    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

class Links(Base):
    __tablename__ = "Links"
    redirect_url: orm.Mapped[str]
    is_active: orm.Mapped[bool] = orm.mapped_column(Boolean, default=True)
    created_at: orm.Mapped[datetime.datetime] = orm.mapped_column(
        DateTime,
        default=datetime.datetime.utcnow,
    )