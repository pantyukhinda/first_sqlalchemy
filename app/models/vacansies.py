from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.metadata import Base


class Vacancies(Base):
    __tablename__ = "vacancies"

    title: Mapped[str]
    compensation: Mapped[int | None]


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

    cover_letter: Mapped[str | None]
