from sqlalchemy import text

from core.database import async_engine, sync_engine


def sync_exec(stmt):
    with sync_engine.connect() as conn:
        result = conn.execute(stmt)
        for row in result.all():
            print(row)


async def async_exec(stmt):
    async with async_engine.connect() as conn:
        result = await conn.execute(stmt)
        for row in result.all():
            print(row)
