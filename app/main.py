import asyncio
from pprint import pprint

from core.crud import (
    create_tables,
    sync_add,
    async_add,
    sync_query,
    async_query,
    async_exec,
    sync_exec,
    async_query_unique,
)

from schemas import ResumesResponse, WorkersResponse, WorkersRelation
from data import Data
from queries import Queries, ComplexDataManipulations

if __name__ == "__main__":
    # Create tables and add data
    create_tables()
    sync_add(Data.workers_data)
    sync_add(Data.resumes_data)
    sync_add(Data.vacancies_data)

    # Bound resumes and vacancies
    ComplexDataManipulations.bound_vacancies_and_resumes()

# async def main():
# # * select_resumes_by_workload
# print(
#     Queries.select_resumes_by_workload().compile(
#         compile_kwargs={"literal_binds": True}
#     )
# )

# task03 = async_query(Queries.select_resumes_by_workload())
# resumes = await task03

# for r in resumes:
#     pprint(r)

# # * join_cte_subquery_window_func
# print(
#     Queries.join_cte_subquery_window_func().compile(
#         compile_kwargs={"literal_binds": True}
#     )
# )

# task04 = async_query(Queries.join_cte_subquery_window_func())
# resumes = await task04

# for r in resumes:
#     pprint(r)

# # * select_workers_with_joined_relationship
# print(
#     Queries.select_workers_with_joined_relationship().compile(
#         compile_kwargs={"literal_binds": True}
#     )
# )
# task05 = async_query_unique(Queries.select_workers_with_joined_relationship())
# resumes = await task05

# for r in resumes:
#     pprint(vars(r[0]))

# # * select_workers_with_selectinload_relationship

# print(
#     Queries.select_workers_with_selectinload_relationship().compile(
#         compile_kwargs={"literal_binds": True}
#     )
# )
# task06 = async_query_unique(Queries.select_workers_with_selectinload_relationship())
# resumes = await task06

# for r in resumes:
#     pprint(r)

# for r in resumes:
#     pprint(r[0].resumes)

# # * select_workers and validate via pydantic
# task07 = async_query(Queries.select_workers())
# workers = await task07
# workers_dto = [
#     WorkersResponse.model_validate(worker["Workers"], from_attributes=True)
#     for worker in workers
# ]
# for w in workers_dto:
#     pprint(w)

# # * select_workers_with_relation and validate via pydantic
# task08 = async_query(Queries.select_workers_with_relation_selectinload())
# workers_rel = await task08
# workers_rel_dto = [
#     WorkersRelation.model_validate(worker, from_attributes=True)
#     for worker in workers_rel
# ]
# for w in workers_rel_dto:
#     pprint(w)


# asyncio.run(main())
