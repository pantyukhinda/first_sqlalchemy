from __future__ import annotations

from pydantic import BaseModel


class WorkersBase(BaseModel):
    name: str


class WorkersCreate(WorkersBase):
    pass


class WorkersResponse(WorkersBase):
    id: int


class WorkersRelation(WorkersResponse):
    resumes: list["ResumesResponse"]
