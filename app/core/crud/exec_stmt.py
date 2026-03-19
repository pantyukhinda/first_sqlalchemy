from sqlalchemy import text

from core.database import async_engine, sync_engine


def sync_exec(stmt):
    with sync_engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
        try:
            return result.all()
        except:
            return None


async def async_exec(stmt):
    async with async_engine.connect() as conn:
        result = await conn.execute(stmt)
        await conn.commit()
        try:
            return result.all()
        except:
            return None


def sync_query(query):
    with sync_engine.connect() as conn:
        result = conn.execute(query)
        return result.all()


async def async_query(query):
    async with async_engine.connect() as conn:
        result = await conn.execute(query)
        return result.all()
