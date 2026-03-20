from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.metadata import Base, created_at, update_at
from . import Workload


class Resumes(Base):
    __tablename__ = "resumes"

    title: Mapped[str]
    compensation: Mapped[int] = mapped_column(nullable=False)
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    created_at: Mapped[created_at]
    updated_ad: Mapped[update_at]
