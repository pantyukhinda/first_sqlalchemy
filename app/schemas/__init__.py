from .resumes import (
    ResumesBase,
    ResumesCreate,
    ResumesResponse,
    ResumesRelation,
)
from .workers import (
    WorkersBase,
    WorkersCreate,
    WorkersResponse,
    WorkersRelation,
)
from .vacancies import (
    VacanciesBase,
    VacanciesCreate,
    VacanciesResponse,
    VacanciesRelation,
)


__all__ = [
    "ResumesBase",
    "ResumesCreate",
    "ResumesResponse",
    "ResumesRelation",
    "WorkersBase",
    "WorkersCreate",
    "WorkersResponse",
    "WorkersRelation",
    "VacanciesBase",
    "VacanciesCreate",
    "VacanciesResponse",
    "VacanciesRelation",
]

WorkersRelation.model_rebuild()
ResumesRelation.model_rebuild()
VacanciesRelation.model_rebuild()
