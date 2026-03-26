from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel

from models import Workload

if TYPE_CHECKING:
    from . import WorkersResponse


class ResumesBase(BaseModel):
    title: str
    compensation: int
    workload: Workload
    worker_id: int


class ResumesCreate(ResumesBase):
    pass


class ResumesResponse(ResumesBase):
    id: int
    created_at: datetime
    updated_ad: datetime


class ResumesRelation(ResumesResponse):
    worker: "WorkersResponse"
