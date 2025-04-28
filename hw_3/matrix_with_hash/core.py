from typing import Any

import numpy as np

from .hash_mixin import HashMixin
from .file_mixin import FileIOMixin


class Matrix(HashMixin, FileIOMixin):
    """
    Класс для работы с матрицами.
    """

    __hash__ = HashMixin.__hash__

    def __init__(self, data: np.ndarray | list[list]):
        """
        Конструктор класса.
        :param data: Матрица в виде двумерного списка, numpy.ndarray
        """
        arr = np.array(data)
        if arr.ndim != 2:
            raise ValueError("Матрица должна быть 2-мерной")
        self.data = arr

    @property
    def shape(self) -> tuple[int, int]:
        """
        Возвращает размерность матрицы

        :return: кортеж из двух чисел, где первое - число строк, второе - число столбцов
        """
        return self.data.shape

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Сложение матриц

        :param other: матрица для сложения
        :return: сумма матриц
        """
        if not isinstance(other, Matrix):
            raise TypeError("Складывать можно только матрицы")
        if self.shape != other.shape:
            raise ValueError("Размерности матриц не совпадают для сложения")
        return Matrix(self.data + other.data)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """
        Покомпонентное умножение матриц

        :param other: матрица для умножения
        :return: результат покомпонентного умножения
        """
        if not isinstance(other, Matrix):
            raise TypeError("Умножать можно только матрицы")
        if self.shape != other.shape:
            raise ValueError("Размерности матриц не совпадают для покомпонентного умножения")
        return Matrix(self.data * other.data)

    @HashMixin.matmul_hash_decorator
    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """
        Матричное умножение двух матриц

        :param other: матрица для умножения
        :return: результат матричного умножения
        """
        if not isinstance(other, Matrix):
            raise TypeError("Умножать можно только матрицы")
        if self.shape[1] != other.shape[0]:
            raise ValueError("Размеры несовместимы для матричного умножения")
        return Matrix(self.data @ other.data)

    def __str__(self) -> str:
        """
        Возвращает строковое представление матрицы

        :return: строка, содержащая матрицу
        """
        matrix_str = [
            [str(cell) for cell in row]
            for row in self.data
        ]
        max_len_cell  = max(
            max(len(str(cell)) for cell in row)
            for row in self.data
        ) + 1
        rows = ['[']
        for row in matrix_str:
            rows.append('\t[ ' + ','.join(cell.rjust(max_len_cell) for cell in row) + ' ],')
        rows.append(']')
        return "\n".join(rows)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Matrix):
            return np.array_equal(self.data, other.data)
        return False
