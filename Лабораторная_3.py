# Есть два типа книг - бумажная и аудио.
# Для всех типов хранения книг у них есть: - название (name) - автор (author)
#
# У бумажной книги есть количество страниц (pages) целочисленного типа данных.
# У аудио книги есть её продолжительность (duration) как числа с плавающей запятой.
#
# Для классов Book, PaperBook, AudioBook примените наследование.
# Исходя из кода подумайте когда методы __str__ и __repr__ могут быть унаследованы,
# а когда перегружены в дочерних классах. И исправьте это
# Атрибуты name и author изменяться не могут, поэтому напишите для них свойства,
# которые не позволят изменять эти атрибуты.
# Так как на pages и duration накладываются ограничения по типу и допустимым значениям,
# напишите для них свойства с проверками при присвоении им значений.


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('Должно быть целочисленным типом данных')
        if value <= 0:
            raise ValueError('Кол-во страниц не может быть отрицательным')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError('Должно быть не целочисленным типом данных')
        if value <= 0:
            raise ValueError('Длительность аудиодорожки не может быть отрицательной')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
