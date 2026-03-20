import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
update_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]


class Base(DeclarativeBase):

    id: Mapped[int] = mapped_column(primary_key=True)
