import asyncio

from sqlalchemy import text

from workers import workers
from core.crud import async_exec
from core.crud import create_tables


if __name__ == "__main__":
    create_tables()

    stmt = text("INSERT INTO workers (id, name) VALUES (1, 'Ivan',), (2, 'Stepan');")
    asyncio.run(async_exec(stmt=stmt))
