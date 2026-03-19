from core.database import database
from core.metadata import metadata_obj


def create_tables():
    metadata_obj.drop_all(database.sync_engine)
    metadata_obj.create_all(database.sync_engine)
