from core.database import database
from core.metadata import Base


def create_tables():
    Base.metadata.drop_all(bind=database.sync_engine)
    Base.metadata.create_all(bind=database.sync_engine)
