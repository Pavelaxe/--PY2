# Итоговое задание
# Выбрать сущности, для которых можно реализовать наследование.
# Например:
# Автомобили — базовый класс. Легковой и грузовой автомобиль —
# дочерние классы.
# Хвойные деревья — базовый класс. Ель и сосна — дочерние классы.
# Социальные сети — базовый класс. VK, Facebook - дочерние классы.
# Должны быть реализованы как минимум один базовый и дочерний класс.
# В базовом классе должны быть реализованы конструктор __init__,
# магические методы __str__ и __repr__.
# В дочернем классе либо унаследовать, либо расширить конструктор базового класса,
# унаследовать или перегрузить магические методы __str__ и __repr__..
# Количество атрибутов и методов для каждого класса выбираете самостоятельно.
# В дочернем классе необходимо унаследовать как минимум один метод и перегрузить
# один метод (помимо магических методов __str__ и __repr__).
# При перегрузке метода обосновать причину, указав её в документации к методу.
# Если считаете необходимым, то некоторые атрибуты и методы можно сделать непубличными.
# Причину инкапсуляции указать или в виде комментариев для атрибутов или в документации
# для методов.
# Все аргументы и выходные результаты методов должны иметь аннотацию типов.
# Для всех классов и методов должна быть написана документация.
# Дополнительно
# Саму реализацию методов писать необязательно.
# Но если считаете возможным описать как бы работали методы, можно представить
# их реализацию в виде python кода.

if __name__ == "__main__":
    class University:
        def __init__(self, name_u: str, city: str):
            """ Изменение названия должно сопровождаться
            проверкой города и наоборот. Поэтому хочу,
            чтоб созданный объект в данных атрибутах был
            неизменным"""
            self._name_u = name_u
            self._city = city

        @property
        def name(self) -> str:
            return self._name_u

        @property
        def city(self) -> str:
            return self._city

        def rating(self) -> int:
            """ Реализация метода через обращение
            к какому-нибудь сайту с рейтингами """
            ...

        def __str__(self) -> str:
            return f"Университет {self.name}. Город {self.city}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name_u={self.name!r}, city={self.city!r})"

    class Institute(University):
        def __init__(self, name_u: str, city: str, location: str, abbreviation: str):
            super().__init__(name_u, city)
            self.location = location
            self._abbreviation = abbreviation

        @property
        def abbreviation(self) -> str:
            return self._abbreviation

        @abbreviation.setter
        def abbreviation(self, value: str) -> None:
            if not isinstance(value, str):
                raise ValueError('Должен быть текст')
            if len(value) == 0:
                raise ValueError('Необходимо добавить аббревиатуру')

        def rating(self) -> int:
            """ Реализация метода,
             но рейтинг уже внутри университета"""
            ...

        def __str__(self) -> str:
            return f"Университет {self.name}. Институт {self.abbreviation}. Город {self.city}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(name_u={self.name!r}, city={self.city!r}," \
                   f" location={self.location!r}, abbreviation={self.abbreviation!r})"
