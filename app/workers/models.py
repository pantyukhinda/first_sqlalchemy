import enum
import datetime
from typing import Annotated
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from core.metadata import Base

created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
update_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]


class Workers(Base):
    __tablename__ = "workers"

    name: Mapped[str] = mapped_column()


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class Resumes(Base):
    __tablename__ = "resumes"

    title: Mapped[str]
    compensation: Mapped[int] = mapped_column(nullable=False)
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(foreign_key="workers.id")
    created_at: Mapped[created_at]
    updated_ad: Mapped[update_at]
