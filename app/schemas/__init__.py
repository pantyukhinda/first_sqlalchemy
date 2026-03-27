from .resumes import ResumesBase, ResumesCreate, ResumesResponse, ResumesRelation
from .workers import WorkersBase, WorkersCreate, WorkersResponse, WorkersRelation


__all__ = [
    "ResumesBase",
    "ResumesCreate",
    "ResumesResponse",
    "ResumesRelation",
    "WorkersBase",
    "WorkersCreate",
    "WorkersResponse",
    "WorkersRelation",
]

WorkersRelation.model_rebuild()
ResumesRelation.model_rebuild()
