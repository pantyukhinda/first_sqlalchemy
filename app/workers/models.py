from sqlalchemy.orm import Mapped, mapped_column

from core.metadata import Base


class Workers(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
