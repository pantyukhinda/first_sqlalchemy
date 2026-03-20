from sqlalchemy import text

from core.database import database


# TODO: Переписать весь код на использование сессий вместо движка
def sync_add(data: list):
    with database.session_factory() as session:
        session.add_all(data)
        session.commit()
