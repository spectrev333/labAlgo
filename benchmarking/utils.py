from collections.abc import Callable
from time import time

def time_call(fun: Callable, args: tuple | list = (), times: int = 1):
    total = 0.0
    for i in range(times):
        start = time()
        fun(*args)
        end = time()
        total += (end - start)
    avg = total / times
    # print("avg exec time %0.3fs. (%d runs)" % (avg, times))
    return avg

def time_call_return(fun: Callable, args: tuple | list = (), times: int = 1):
    total = 0.0
    res = None
    for i in range(times):
        start = time()
        res = fun(*args)
        end = time()
        total += (end - start)
    avg = total / times
    # print("avg exec time %0.3fs. (%d runs)" % (avg, times))
    return avg, res