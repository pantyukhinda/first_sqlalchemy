import asyncio


from core import database
from workers import Workers
from core.crud import sync_add, create_tables


if __name__ == "__main__":
    create_tables()

    worker_ivan: Workers = Workers(name="Ivan")

    sync_add(
        [
            worker_ivan,
        ]
    )
