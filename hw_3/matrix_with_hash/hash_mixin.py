import functools
from typing import Any, Callable, Hashable, TypeVar

import numpy as np


class HashMixin:
    """
    Миксин для реализации функции хеширования матриц
    """

    def __hash__(self) -> int:
        """
        Простейшая хеш-функция: для каждого элемента берём его хеш,
        умножаем на линейный индекс (i * num_cols + j + 1) и складываем по XOR.
        Это даёт ненулевую, не-константную функцию.
        """
        n_rows, n_cols = self.data.shape
        result = 0
        for i in range(n_rows):
            for j in range(n_cols):
                idx = i * n_cols + j + 1
                result ^= int(self.data[i, j]) * idx
        return result

    @classmethod
    def matmul_hash_decorator(cls, func: Callable) -> Callable:
        cache: dict[tuple[int, int], Hashable] = {}

        @functools.wraps(func)
        def wrapper(a: Hashable, b: Hashable) -> Hashable:
            nonlocal cache
            hashes = hash(a), hash(b)
            if hashes not in cache:
                cache[hashes] = func(a, b)
            return cache[hashes]

        return wrapper
