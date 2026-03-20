from sqlalchemy.orm import Mapped, mapped_column

from core.metadata import Base


class Workers(Base):
    __tablename__ = "workers"

    name: Mapped[str] = mapped_column()
