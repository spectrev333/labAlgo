from collections.abc import Callable
from time import time
import numpy as np
from scipy.stats import zscore


class TestBench:

    def run_all(self):
        pass

    @classmethod
    def bench(cls, fun: Callable, times: int = 1):
        total = 0.0
        for i in range(times):
            start = time()
            fun()
            end = time()
            total += (end - start)
        avg = total / times
        #print("avg exec time %0.3fs. (%d runs)" % (avg, times))
        return avg

    @classmethod
    def time_call(cls, fun: Callable, args: tuple | list, times: int = 1):
        total = 0.0
        for i in range(times):
            start = time()
            fun(*args)
            end = time()
            total += (end - start)
        avg = total / times
        #print("avg exec time %0.3fs. (%d runs)" % (avg, times))
        return avg

    @classmethod
    def moving_average(cls, data, window_size=5):
        return np.convolve(data, np.ones(window_size) / window_size, mode='valid')

    @classmethod
    def filter_outliers(cls, data):
