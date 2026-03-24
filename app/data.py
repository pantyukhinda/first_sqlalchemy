from models import Workers, Resumes


class Data:
    workers_data: list[Workers] = [
        Workers(name="Ivan"),
        Workers(name="Stepan"),
        Workers(name="Petr"),
    ]

    resumes_data: list[Resumes] = [
        Resumes(
            title="Python junior developer",
            compensation=60_000,
            workload="fulltime",
            worker_id=1,
        ),
        Resumes(
            title="Python Developer",
            compensation=70_000,
            workload="fulltime",
            worker_id=1,
        ),
        Resumes(
            title="Python Data Engineer",
            compensation=80_000,
            workload="parttime",
            worker_id=2,
        ),
        Resumes(
            title="Data scientist",
            compensation=90_000,
            workload="fulltime",
            worker_id=2,
        ),
        Resumes(
            title="Python Analyst",
            compensation=100_000,
            workload="fulltime",
            worker_id=3,
        ),
    ]
