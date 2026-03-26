from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.metadata import Base

if TYPE_CHECKING:
    from . import Resumes


class Workers(Base):
    __tablename__ = "workers"

    name: Mapped[str] = mapped_column()

    # relationship
    resumes: Mapped[list["Resumes"]] = relationship(back_populates="worker")
