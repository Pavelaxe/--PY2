# Написать класс Library, конструктор которого будет инициализировать следующие атрибуты:
#
# books - Список книг
# Конструктор должен принимать необязательный аргумент со значением по умолчанию.
# Если пользователь его не передал, то библиотека инициализируется с пустым списком книг.
#
# В классе должен быть объявлен метод get_next_book_id.
# Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
# Если книг в библиотеке нет, то вернуть 1.
# Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
#
# В классе должен быть объявлен метод get_index_by_book_id.
# Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
# Если книга существует, то вернуть индекс из списка.
# Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'
        # TODO написать класс Book


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, index: int):
        for index_, value in enumerate(self.books):
            if index_+1 == index:
                return index_
        raise ValueError('Книги с запрашиваемым id не существует')
                # TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
