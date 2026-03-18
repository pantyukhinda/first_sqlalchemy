import asyncio

from sqlalchemy import text

from core.database import async_engine, sync_engine

with sync_engine.connect() as conn:
    query = text("SELECT * FROM pg_database")
    result = conn.execute(query)
    for row in result.all():
        print(row)


async def select_query(query):
    async with async_engine.connect() as conn:
        result = await conn.execute(query)
        for row in result.all():
            print(row)


if __name__ == "__main__":

    async def main():
        query = text("SELECT * FROM pg_database")
        asyncio.run(select_query(query=query))
