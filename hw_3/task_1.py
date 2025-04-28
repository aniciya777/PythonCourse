import numpy as np

from hw_3.matrix import Matrix

if __name__ == "__main__":
    np.random.seed(0)

    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))

    sum_matrix = m1 + m2
    elem_mul_matrix = m1 * m2
    mat_mul_matrix = m1 @ m2

    with open("artifacts/hw_3_1/matrix+.txt", "w", encoding="utf-8") as f:
        f.write(str(sum_matrix))
    with open("artifacts/hw_3_1/matrix*.txt", "w", encoding="utf-8") as f:
        f.write(str(elem_mul_matrix))
    with open("artifacts/hw_3_1/matrix@.txt", "w", encoding="utf-8") as f:
        f.write(str(mat_mul_matrix))
