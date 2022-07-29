from dataclasses import dataclass
from typing import List


@dataclass
class Book():
    title: str
    author: str
    price: float


@dataclass
class Shelf():
    books: List[Book]

    def total_price(
        self
    ) -> float:
        return sum([book.price for book in self.books])


def main():
    b1 = Book('b1', 'a1', 100.123)
    b2 = Book('b2', 'a2', 200.123)
    b3 = Book('b3', 'a3', 300.123)

    shelf = Shelf([b1, b2, b3])
    print(shelf)

    total_price = shelf.total_price()
    print(f'{total_price=}')


if __name__ == '__main__':
    main()
