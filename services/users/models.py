from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.base.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]

    cases: Mapped[List["Case"]] = relationship(
        back_populates="creator", cascade="all, delete"
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
