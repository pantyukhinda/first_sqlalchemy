from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.metadata import Base

if TYPE_CHECKING:
    from . import Resumes


class Vacancies(Base):
    __tablename__ = "vacancies"

    title: Mapped[str]
    compensation: Mapped[int | None]

    # relationships
    resumes_replied: Mapped[list["Resumes"]] = relationship(
        back_populates="vacancies_replied",
        secondary="vacancies_replies",
    )


class VacanciesReplies(Base):
    __tablename__ = "vacancies_replies"

    resume_id: Mapped[int] = mapped_column(
        ForeignKey(
            "resumes.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        primary_key=True,
    )

    cover_letter: Mapped[Optional[str]] = mapped_column(nullable=True)
