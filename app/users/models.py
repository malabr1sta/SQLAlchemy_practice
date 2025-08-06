from typing import List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class City(Base):
    __tablename__ = "city"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str] = mapped_column(String(50), nullable=False)
    days_delivery: Mapped[int] = mapped_column(Integer, default=0)

    clients: Mapped[List["Client"]] = relationship(
        back_populates="city", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"City(city_id={self.city_id}, name_city={self.name_city})"


class Client(Base):
    __tablename__ = "client"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    name_client: Mapped[str] = mapped_column(String(100), nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.city_id"))

    city: Mapped["City"] = relationship(
        back_populates="clients", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Client(client_id={self.client_id}, email={self.email})"
