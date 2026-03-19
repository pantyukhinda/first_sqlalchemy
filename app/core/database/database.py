from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine


from core.config import settings


class DataBase:
    """Provides access to the database"""

    def __init__(self):
        self.sync_engine = create_engine(
            url=settings.db.sync_url,
            echo=settings.db.echo,
            pool_size=settings.db.pool_size,
        )

        self.async_engine = create_async_engine(
            url=settings.db.async_url,
            echo=settings.db.echo,
            pool_size=settings.db.pool_size,
        )

        self.session_factory = sessionmaker(
            bind=self.sync_engine,
            class_=Session,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

        self.async_session_factory = async_sessionmaker(
            bind=self.async_engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


database = DataBase()
