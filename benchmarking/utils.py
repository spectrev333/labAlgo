from collections.abc import Callable
from time import perf_counter
import numpy as np

def time_call(fun: Callable, args: tuple | list = (), times: int = 1):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        fun(*args)
        end = perf_counter()
        total += (end - start)
    avg = total / times
    # print("avg exec time %0.3fs. (%d runs)" % (avg, times))
    return avg

def time_call_return(fun: Callable, args: tuple | list = (), times: int = 1):
    total = 0.0
    res = None
    for i in range(times):
        start = perf_counter()
        res = fun(*args)
        end = perf_counter()
        total += (end - start)
    avg = total / times
    # print("avg exec time %0.3fs. (%d runs)" % (avg, times))
    return avg, res