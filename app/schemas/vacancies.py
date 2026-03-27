from __future__ import annotations

from pydantic import BaseModel


class VacanciesBase(BaseModel):
    title: str
    compensation: int


class VacanciesCreate(VacanciesBase):
    pass


class VacanciesResponse(VacanciesBase):
    id: int


class VacanciesRelation(VacanciesResponse):
    resumes_replied: list["ResumesResponse"]
