from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text


from core.config import settings


# class DataBase:
#     """Provides access to the database"""

#     def __init__(self):
#         self.engine = create_async_engine(
#             url=settings.db.async_url,
#             echo=settings.db.echo,
#         )

#         self.session_factory = async_sessionmaker(
#             bind=self.engine,
#             class_=AsyncSession,
#             autoflush=False,
#             autocommit=False,
#             expire_on_commit=False,
#         )

engine = create_engine(
    url=settings.db.sync_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
)


# database = DataBase()
