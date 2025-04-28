from numpy.lib.mixins import NDArrayOperatorsMixin
import numpy as np

from .mixins import StringMixin, FileIOMixin, PropertyMixin


class Matrix(NDArrayOperatorsMixin, StringMixin, FileIOMixin, PropertyMixin):
    """
    Класс для представления и работы с матрицами

    Attributes:
        array (numpy.ndarray): двумерный массив, представляющий матрицу
    """
    __fields__ = ['array']
    __array_priority__ = 20.0

    def __init__(self, data):
        self._array = np.array(data)

    def __array__(self, dtype=None):
        return np.array(self._array, dtype=dtype)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        arrays = []
        for input_ in inputs:
            if isinstance(input_, Matrix):
                arrays.append(input_._array)
            else:
                arrays.append(input_)
        result = getattr(ufunc, method)(*arrays, **kwargs)
        if isinstance(result, tuple):
            return tuple(Matrix(res) for res in result)
        return Matrix(result)
