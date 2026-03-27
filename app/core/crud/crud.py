from sqlalchemy import text

from core.database import database


def sync_add(data: list):
    with database.session_factory() as session:
        session.add_all(data)
        session.commit()


async def async_add(data: list):
    async with database.async_session_factory() as session:
        session.add_all(data)
        await session.commit()


def sync_exec(query):
    with database.session_factory() as session:
        session.execute(query)
        session.commit()


async def async_exec(query):
    async with database.async_session_factory() as session:
        await session.execute(query)
        await session.commit()


def sync_query(query):
    with database.session_factory() as session:
        result = session.execute(query)
        return result.scalars().all()


async def async_query(query):
    async with database.async_session_factory() as session:
        result = await session.execute(query)
        return result.scalars().all()


async def async_query_unique(query):
    async with database.async_session_factory() as session:
        result = await session.execute(query)
        return result.unique().all()


async def async_query_unique_scalars(query):
    async with database.async_session_factory() as session:
        result = await session.execute(query)
        return result.unique().scalars().all()
