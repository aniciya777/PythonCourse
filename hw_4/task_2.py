import enum
import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import wraps
from typing import Callable

import matplotlib.pyplot as plt


def time_decorator(function: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции

    :param function: функция для измерения времени выполнения
    :return: время выполнения функции
    """

    @wraps(function)
    def wrapper(*args, **kwargs) -> float:
        start = time.perf_counter()
        function(*args, **kwargs)
        end = time.perf_counter()
        return end - start

    return wrapper


def _integrate_chunk(args: tuple[Callable[[float], float], float, float, int, int, int]) -> float:
    """
    Функция, выполняемая каждым воркером

    args = (f, a, b, n_iter, start, end)
    """
    f, a, b, n_iter, start, end = args
    step = (b - a) / n_iter
    acc = 0.0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


class Executor(enum.StrEnum):
    THREAD = 'thread'
    PROCESS = 'process'


@time_decorator
def integrate(
        f: Callable[[float], float],
        a: float,
        b: float,
        n_jobs: int,
        n_iter: int,
        executor: Executor):
    """
    Параллельное интегрирование методом прямоугольников.

    :param f:        функция (например, math.cos)
    :param a, b:     границы интегрирования
    :param n_jobs:   число воркеров
    :param n_iter:   сколько точек считать
    :param executor: 'thread' или 'process'
    """
    # разбиваем 0..n_iter на n_jobs диапазонов
    chunk_size = n_iter // n_jobs
    tasks = []
    for j in range(n_jobs):
        start = j * chunk_size
        end = (j + 1) * chunk_size if j < n_jobs - 1 else n_iter
        tasks.append((f, a, b, n_iter, start, end))
    Executor = ThreadPoolExecutor if executor == 'thread' else ProcessPoolExecutor
    with Executor(max_workers=n_jobs) as pool:
        results = pool.map(_integrate_chunk, tasks)
    return sum(results)


if __name__ == '__main__':
    cpu_num = os.cpu_count() or 1
    n_iter = 10_000_000
    x_list = []
    thread_list = []
    process_list = []
    with open('artifacts/task_2.md', 'w', encoding='utf-8') as file:
        print("| n_jobs | Time (sec) thread | Time (sec) process |")
        print("|--------|-------------------|--------------------|")
        print("| n_jobs | Time (sec) thread | Time (sec) process |", file=file)
        print("|--------|-------------------|--------------------|", file=file)
        for n_jobs in range(1, cpu_num * 2 + 1):
            val1 = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter, executor='thread')
            val2 = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter, executor='process')
            x_list.append(n_jobs)
            thread_list.append(val1)
            process_list.append(val2)
            print(f"| {n_jobs} | {val1:.4f} | {val2:.4f} |")
            print(f"| {n_jobs} | {val1:.4f} | {val2:.4f} |", file=file)
        plt.plot(x_list, process_list, label='process')
        plt.plot(x_list, thread_list, label='thread')
        plt.xlabel('Количество воркеров')
        plt.ylabel('Время выполнения (секунды)')
        plt.title('Зависимость времени выполнения от количества воркеров')
        plt.legend()
        plt.savefig('artifacts/task_2.png')
