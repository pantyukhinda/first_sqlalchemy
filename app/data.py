from models import Workers, Resumes


class Data:
    workers_data: list[Workers] = [
        Workers(name="Ivan"),
        Workers(name="Stepan"),
    ]

    resumes_data: list[Resumes] = [
        Resumes(
            title="Ivan's resume",
            compensation=100_000,
            workload="parttime",
            worker_id=1,
        ),
        Resumes(
            title="Stepan's resume",
            compensation=150_000,
            workload="fulltime",
            worker_id=2,
        ),
    ]
