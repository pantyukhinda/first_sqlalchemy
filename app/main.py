import asyncio
from pprint import pprint
from sqlalchemy import select, update

from core.crud import (
    create_tables,
    sync_add,
    async_add,
    async_query,
    async_exec,
)
from models import Resumes
from data import Data


if __name__ == "__main__":
    create_tables()
    sync_add(Data.workers_data)


async def main():
    task01 = async_add(Data.resumes_data)
    task02 = async_query(select(Resumes))

    await task01
    resumes = await task02

    for r in resumes:
        pprint(vars(r))

    task03 = async_exec(
        update(Resumes).values(title="STEPAN'S RESUME").filter_by(worker_id=2)
    )

    await task03

    task04 = async_query(select(Resumes))

    resumes = await task04

    for r in resumes:
        pprint(vars(r))


asyncio.run(main())
