from sqlalchemy import Table, Column, Integer, String

from core.metadata import metadata_obj

workers = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)
