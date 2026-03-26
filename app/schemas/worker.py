from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from . import ResumesResponse


class WorkersBase(BaseModel):
    name: str


class WorkersCreate(WorkersBase):
    pass


class WorkersResponse(WorkersBase):
    id: int


class WorkersRelation(WorkersResponse):
    resumes: list["ResumesResponse"]
