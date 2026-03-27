from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel

from models import Workload


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
    updated_at: datetime


class ResumesRelation(ResumesResponse):
    worker: "WorkersResponse"
