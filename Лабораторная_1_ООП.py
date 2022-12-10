import doctest


class CopyBook:
    def __init__(self, type_: str, papers: int, filled_pages: int):
        """
        Инициализация атрибутов для объектов типа "Тетрадь"
        :param type_: Размер тетради и её тип (в клетку, линейку...)
        :param papers: Количество листов в тетради
        :param filled_pages: Количество уже исписанных листов

        Примеры:
        >>> copy_book_1 = CopyBook('A5 вклетку', 96, 53) # Инициализация экемпляра класса
        """
        if not isinstance(type_, str):
            raise TypeError('Тип тетради это строка')
        if not isinstance(papers, int):
            raise TypeError('Количество страниц выражается целочисленно')
        if papers <= 0:
            raise ValueError('Количество страниц должно быть положительным')
        self.type = type_
        self.quantity_of_papers = papers
        self.empty_papers = None
        self.init_empty_papers(filled_pages)

    def init_empty_papers(self, filled_pages: int):
        """
        Метод инициализирует значение атрибута empty_papers
        :param filled_pages: Количество исписанных страниц

        Примеры:
        >>> copy_book_2 = CopyBook('A4 для рисования', 24, 12)
        >>> copy_book_2.init_empty_papers(12)
        """
        if not isinstance(filled_pages, int):
            raise TypeError('Исписанными считаются целые страницы')
        if filled_pages < 0:
            raise ValueError('Количество заполненный страниц не может быть отрицательным')
        self.empty_papers = self.quantity_of_papers - filled_pages

    def is_new(self, filled_pages: int) -> bool:
        """
        Метод, который проверяет, пустая ли тетрадка
        """
        if not isinstance(filled_pages, int):
            raise TypeError('Исписанными считаются целые страницы')
        if filled_pages < 0:
            raise ValueError('Количество заполненный страниц не может быть отрицательным')
        if self.quantity_of_papers - filled_pages == 0:
            return True


class Concert:
    def __init__(self, capacity: int, price_of_ticket: float):
        """
        Инициализация атрибутов для объектов типа "Концерт"
        :param capacity: Вместимость зала
        :param price_of_ticket: Стоимость билета

        Примеры:
        >>> crocus = Concert(30000, 2500.0)
        """
        if not isinstance(capacity, int):
            raise TypeError
        if not isinstance(price_of_ticket, float):
            raise TypeError
        if capacity < 0:
            raise ValueError
        if price_of_ticket < 0:
            raise ValueError
        self.capacity = capacity
        self.price = price_of_ticket
        self.max_income = capacity * price_of_ticket

    def current_income(self, quantity_of_sold_tickets: int) -> float:
        """
        Метод расчёта текущей выручки
        :param quantity_of_sold_tickets: Количество проданных билетов
        :return: Текущая выручка от проданных билетов
        """
        if not isinstance(quantity_of_sold_tickets, int):
            raise TypeError
        if quantity_of_sold_tickets < 0:
            raise ValueError
        ...

    def expenses(self, estimate: dict) -> float:
        """
        Метод расчёта сметы концерта
        :param estimate: Словарь со статьями расхода и самими расходами
        :return: Себестоимость концерта
        """
        ...

class Test:
    def __init__(self, tasks: dict, list_of_possible_marks: list, time_limit: int):
        """
        Инициализация атрибутов для объектов типа "Тест"
        :param tasks: Словарь с вопросами и ответами
        :param list_of_possible_marks: Возможные оценки для выбора
        :param time_limit: Временные ограничения на тест, в минутах

        Пример:
        >>> math = Test({'Кто сказал...' : 'Марков'}, [3, 4, 5], 120)
        """
        if not isinstance(tasks, dict):
            raise TypeError('Только словари')
        if not isinstance(list_of_possible_marks, list):
            raise TypeError('Хотелось бы получить список')
        if not isinstance(time_limit, int):
            raise TypeError('Целочисленный лимит времени')
        if time_limit < 0:
            raise ValueError('Лимит не может быть отрицательным')
        self.tasks = tasks
        self.list_of_possible_marks = list_of_possible_marks
        self.time_limit = time_limit

    def average_time_per_question(self) -> float:
        '''
        Метод для определения среднего времени на вопрос
        :return: вернёт вещественное число количества минут
        '''
        ...

    def scoring(self) -> dict:
        '''
        Метод для определения разбаловки конкретных оценок
        :return: вернёт словарь разбаловки
        '''
        ...

if __name__ == "__main__":
    doctest.testmod()
