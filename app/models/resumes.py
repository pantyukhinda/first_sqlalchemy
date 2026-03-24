from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.metadata import Base, created_at, update_at
from . import Workload

if TYPE_CHECKING:
    from . import Workers


class Resumes(Base):
    __tablename__ = "resumes"

    title: Mapped[str]
    compensation: Mapped[int] = mapped_column(nullable=False)
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    created_at: Mapped[created_at]
    updated_ad: Mapped[update_at]

    worker: Mapped["Workers"] = relationship()
