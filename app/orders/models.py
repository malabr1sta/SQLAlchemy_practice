from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Buy(Base):
    __tablename__ = "buy"

    buy_id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[int] = mapped_column(String(150), nullable=True)
    clien_id: Mapped[int] = mapped_column(ForeignKey("client.client_id"))

    buy_steps: Mapped[List["BuyStep"]] = relationship(
        back_populates="buy", lazy="raise_on_sql"
    )
    buy_books: Mapped[List["BuyBook"]] = relationship(
        back_populates="buy", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Buy(buy_id={self.buy_id})"


class Step(Base):
    __tablename__ = "step"

    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str] = mapped_column(String(50))

    buy_steps: Mapped[List["BuyStep"]] = relationship(
        back_populates="step", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Step(step_id={self.step_id}, name_step={self.name_step})"


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    date_step_beg: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    date_step_end: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True
    )

    buy: Mapped["Buy"] = relationship(
        back_populates="buy_steps",
        lazy="raise_on_sql"
    )
    step: Mapped["Step"] = relationship(
        back_populates="buy_steps",
        lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return (f"BuyStep(buy_step_id={self.buy_step_id},"
                f"date_step_beg={self.date_step_beg},"
                f"date_step_end={self.date_step_end})")


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.book_id"))
    amount: Mapped[int] = mapped_column(Integer, default=1)

    book: Mapped["Book"] = relationship(
        back_populates="buy_books",
        lazy="raise_on_sql"
    )
    buy: Mapped["Buy"] = relationship(
        back_populates="buy_books",
        lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"BuyBook(buy_book_id={self.buy_book_id}, book_id={self.book_id})"
