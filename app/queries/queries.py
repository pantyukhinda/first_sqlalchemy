from sqlalchemy import Integer, and_, cast, func, select
from sqlalchemy.orm import aliased, joinedload
from models import Resumes, Workers


class Queries:
    @staticmethod
    def select_resumes_by_workload():
        select_resumes = (
            select(
                Resumes.workload,
                cast(func.avg(Resumes.compensation), Integer).label(
                    "avg_compensations"
                ),
            )
            .select_from(Resumes)
            .where(and_(Resumes.title.contains("Python"), Resumes.compensation > 40000))
            .group_by(Resumes.workload)
            .having(cast(func.avg(Resumes.compensation), Integer) > 70000)
        )
        return select_resumes

    @staticmethod
    def join_cte_subquery_window_func():
        r = aliased(Resumes)
        w = aliased(Workers)

        subq = (
            select(
                w,
                r,
                func.avg(r.compensation)
                .over(partition_by=r.workload)
                .cast(Integer)
                .label("avg_workload_compensation"),
            )
            .select_from(w)
            .join(r, r.worker_id == w.id)
            .subquery("helper01")
        )

        cte = select(
            subq.c.worker_id,
            subq.c.name,
            subq.c.compensation,
            subq.c.workload,
            subq.c.avg_workload_compensation,
            (subq.c.compensation - subq.c.avg_workload_compensation).label(
                "compensation_diff"
            ),
        ).cte("helper02")

        query = select(cte).order_by(cte.c.compensation_diff.desc())

        return query

    @staticmethod
    def select_workers_with_joined_relationship():
        workers_with_relationship = select(Workers).options(joinedload(Workers.resume))

        return workers_with_relationship
