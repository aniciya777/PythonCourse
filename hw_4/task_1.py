import threading
import multiprocessing
import time
from functools import wraps
from typing import Callable


def fib(n: int) -> int:
    """
    Вычисления числа Фибоначчи

    :param n: число Фибоначчи, которое нужно посчитать
    :return: число Фибоначчи
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def time_decorator(function: Callable[[int, int], None]) -> Callable[[int, int], float]:
    @wraps(function)
    def wrapper(n: int, runs: int) -> float:
        start = time.perf_counter()
        function(n, runs)
        end = time.perf_counter()
        return end - start

    return wrapper


@time_decorator
def synchronous(n: int, runs: int) -> None:
    """
    Вычисление числа Фибоначчи последовательно

    :param n: число Фибоначчи, которое нужно посчитать
    :param runs: количество запусков
    """
    for _ in range(runs):
        fib(n)


@time_decorator
def threading_run(n: int, runs: int) -> None:
    """
    Вычисление числа Фибоначчи параллельно с использованием потоков

    :param n: число Фибоначчи, которое нужно посчитать
    :param runs: количество запусков
    """
    threads = []
    for _ in range(runs):
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


@time_decorator
def multiprocessing_run(n: int, runs: int) -> None:
    """
    Вычисление числа Фибоначчи параллельно с использованием процессов

    :param n: число Фибоначчи, которое нужно посчитать
    :param runs: количество запусков
    """
    processes = []
    for _ in range(runs):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def main():
    n = 36
    runs = 10
    print(f"Вычисляем числа Фибоначчи {runs} раз, каждый раз до числа {n}.")
    sync_time = synchronous(n, runs)
    thread_time = threading_run(n, runs)
    process_time = multiprocessing_run(n, runs)
    results = (
        f"Синхронное вычисление заняло:                 {sync_time:.4f} секунд\n"
        f"Вычисление с использованием потоков заняло:   {thread_time:.4f} секунд\n"
        f"Вычисление с использованием процессов заняло: {process_time:.4f} секунд"
    )
    with open("artifacts/task_1.txt", "w", encoding="utf-8") as f:
        print(f"Вычисляем числа Фибоначчи {runs} раз, каждый раз до числа {n}.\n", file=f)
        print(results, file=f)
        print(results)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
