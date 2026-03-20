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
