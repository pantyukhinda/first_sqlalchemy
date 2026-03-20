import asyncio


from workers import Workers, Resumes
from core.crud import create_tables, sync_add, async_add


if __name__ == "__main__":
    create_tables()

    worker_ivan: Workers = Workers(name="Ivan")
    worker_stepan: Workers = Workers(name="Stepan")

    resume_ivan: Resumes = Resumes(
        title="Ivan's resume",
        compensation=100_000,
        workload="parttime",
        worker_id=1,
    )

    resume_stepan: Resumes = Resumes(
        title="Stepan's resume",
        compensation=150_000,
        workload="fulltime",
        worker_id=2,
    )

    sync_add(
        [
            worker_ivan,
            worker_stepan,
        ]
    )

    asyncio.run(
        async_add(
            [
                resume_ivan,
                resume_stepan,
            ]
        )
    )
