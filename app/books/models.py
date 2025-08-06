from decimal import Decimal
from typing import List

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Author(Base):
    __tablename__ = "author"

    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str] = mapped_column(String(50), nullable=False)

    books: Mapped[List["Book"]] = relationship(
        back_populates="author", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Author(author_id={self.author_id}, name_author={self.name_author})"


class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str] = mapped_column(String(100), nullable=False)

    books: Mapped[List["Book"]] = relationship(
        back_populates="genre", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Genre(genre_id={self.genre_id}, name_genre={self.name_genre})"


class Book(Base):
    __tablename__ = "book"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(16, 2), default=Decimal("0.00"))
    amount: Mapped[int] = mapped_column(Integer, default=0)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.genre_id"))

    author: Mapped["Author"] = relationship(
        back_populates="books", lazy="raise_on_sql"
    )
    genre: Mapped["Genre"] = relationship(
        back_populates="books", lazy="raise_on_sql"
    )
    buy_books: Mapped[List["BuyBook"]] = relationship(
        back_populates="book", lazy="raise_on_sql"
    )

    def __repr__(self) -> str:
        return f"Book(book_id={self.book_id}, title={self.title})"
