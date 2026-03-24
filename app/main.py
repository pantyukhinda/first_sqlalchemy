import asyncio
from pprint import pprint

from core.crud import (
    create_tables,
    sync_add,
    async_add,
    async_query,
    async_exec,
    sync_exec,
    async_query_unique,
)

from data import Data
from queries import Queries

if __name__ == "__main__":
    create_tables()
    sync_add(Data.workers_data)
    sync_add(Data.resumes_data)


async def main():

    print(
        Queries.select_resumes_by_workload().compile(
            compile_kwargs={"literal_binds": True}
        )
    )

    task03 = async_query(Queries.select_resumes_by_workload())
    resumes = await task03

    for r in resumes:
        pprint(r)

    print(
        Queries.join_cte_subquery_window_func().compile(
            compile_kwargs={"literal_binds": True}
        )
    )

    task04 = async_query(Queries.join_cte_subquery_window_func())
    resumes = await task04

    for r in resumes:
        pprint(r)

    print(
        Queries.select_workers_with_joined_relationship().compile(
            compile_kwargs={"literal_binds": True}
        )
    )
    task05 = async_query_unique(Queries.select_workers_with_joined_relationship())
    resumes = await task05

    for r in resumes:
        pprint(vars(r[0]))


asyncio.run(main())
