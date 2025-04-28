import math


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


if __name__ == '__main__':
    print(integrate(math.cos, 0, math.pi / 2))
