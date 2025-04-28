from itertools import product

import numpy as np

from matrix_with_hash import Matrix


def find_collision(
        value_range: range = range(-1, 3),
        shape: tuple[int, int] = (2, 2)
    ) -> tuple[Matrix, Matrix, int] | tuple[None, None, None]:
    """
    Находит коллизию для произведения матриц из заданного диапазона значений и формы.

    :param value_range: диапазон значений для элементов матрицы
    :param shape: форма матрицы (количество строк, количество столбцов)
    :return: матрицы A, C, хеш-значение коллизии, либо (None, None, None) если не найдено
    """
    seen = {}
    for entries in product(value_range, repeat=shape[0] * shape[1]):
        arr = np.array(entries).reshape(shape)
        M = Matrix(arr)
        h = hash(M)
        if h in seen and not np.array_equal(M.data, seen[h].data):
            return seen[h], M, h
        seen[h] = M
    return None, None, None


A, C, collision_hash = find_collision()
if A is None:
    raise RuntimeError("Не удалось найти коллизию за заданный диапазон")
B = Matrix([[1, 0], [0, 1]])  # единичная матрица
D = B

# Вычисляем результат с кэшем (AB) и истинный результат для C @ D (CD_true)
AB = A @ B  # используем кэш при вычислении
CD = C @ D  # используем кэш при вычислении
CD_true = Matrix(C.data @ D.data)  # обход кэша, чтобы получить настоящий результат

# Сохраняем матрицы и результаты
base_path = 'artifacts/hw_3_3'
A.to_file(f'{base_path}/A.txt')
B.to_file(f'{base_path}/B.txt')
C.to_file(f'{base_path}/C.txt')
D.to_file(f'{base_path}/D.txt')
AB.to_file(f'{base_path}/AB.txt')
CD_true.to_file(f'{base_path}/CD.txt')

# Хеши результатов AB и CD_true
hash_AB = hash(AB)
hash_CD = hash(CD_true)
with open(f'{base_path}/hash.txt', 'w') as f:
    f.write(f"{hash_AB}\n{hash_CD}\n")

print("Найденная коллизия:")
print("A = ", A)
print("C = ", C)
print("AB = ", AB)
print("CD = ", CD)
print("CD_true = ", CD_true)
print("hash(A) == hash(C) == ", hash(A))

assert ((hash(A) == hash(C)) and (A != C) and (B == D))
assert (A @ B == C @ D) and (Matrix(A.data @ B.data) != Matrix(C.data @ D.data))
