from app.books.models import Author, Book, Genre
from app.database import Base, engine
from app.orders.models import Buy, BuyBook, BuyStep, Step
from app.users.models import City, Client


def init_db() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print(Base.metadata.tables.keys())

def main() -> None:
    init_db()


if __name__ == "__main__":
    main()
