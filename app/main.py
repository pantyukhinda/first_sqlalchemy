import asyncio

from sqlalchemy import text, insert, select

from workers import workers
from core.crud import async_exec, sync_query
from core.crud import create_tables


if __name__ == "__main__":
    create_tables()

    # stmt = text(
    #     "INSERT INTO workers (id, name) VALUES (1, 'Ivan'), (2, 'Stepan') RETURNING *;"
    # )
    # query = text("SELECT * FROM workers WHERE id > 3;")
    stmt = insert(workers).values(
        [
            {"name": "Ivan"},
            {"name": "Stepan"},
        ]
    )

    query = select(workers)
    asyncio.run(async_exec(stmt=stmt))
    result = sync_query(query=query)
    print(result)
