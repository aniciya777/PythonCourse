import numpy as np


class StringMixin:
    """
    Миксин для работы с текстовым представлением матрицы
    """

    def __str__(self) -> str:
        """
        Возвращает строковое представление матрицы

        :return: строка, содержащая матрицу
        """
        matrix_str = [
            [str(cell) for cell in row]
            for row in self._array
        ]
        max_len_cell = max(
            max(len(str(cell)) for cell in row)
            for row in self._array
        ) + 1
        rows = ['[']
        for row in matrix_str:
            rows.append('\t[ ' + ','.join(cell.rjust(max_len_cell) for cell in row) + ' ],')
        rows.append(']')
        return "\n".join(rows)


class FileIOMixin:
    """
    Миксин для работы с файлами
    """

    def to_file(self, filename: str) -> None:
        """
        Сохраняет строковое представление объекта в файл

        :param filename: путь к файлу
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(self))


class PropertyMixin:
    """
    Миксин для работы с полями
    """

    def __init_subclass__(cls):
        """
        Метод вызывается при создании подкласса
        Автоматически добавляет геттеры/сеттеры для полей, указанных в `__fields__`
        """
        super().__init_subclass__()
        fields = getattr(cls, '__fields__', [])
        for name in fields:
            private = f'_{name}'

            def make_getter(n):
                return lambda self: getattr(self, f'_{n}')

            def make_setter(n):
                return lambda self, value: setattr(self, f'_{n}', value)

            setattr(cls, name, property(make_getter(name), make_setter(name)))
