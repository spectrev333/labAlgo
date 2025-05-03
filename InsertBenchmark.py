from trees.BoolBTree import BoolBTree
from trees.LLBTree import LLBTree
from benchmarking.utils import time_call
from benchmarking.BenchDataGenerator import BenchDataGenerator
from trees.BTree import BTree
import matplotlib.pyplot as plt
import numpy as np
from timeseries import Timeseries, filter_outliers, moving_average



class InsertBenchmark:
    def __init__(self, tree):
        super()
        self.tree = tree
        self.last_run = None
        self.gen = None

    def run_all(self):
        self.last_run = {
            # "Insert 1000 duplicates": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 1_000, 1.0, (1, 200)),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000, 1.0, (1, 200)),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000, 1.0, (1, 200))
            # },
            # "Insert 10000 duplicates": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 10_000, 1.0, (1, 200)),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 10_000, 1.0, (1, 200)),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 10_000, 1.0, (1, 200))
            # },
            # "Insert 1000000 duplicates": {
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000_000, 1.0, (1, 200), 100),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000_000, 1.0, (1, 200), 100)
            # },
            "Insert 1000 elements 0.25 duplication rate": {
                "BTree": self.insert_bench_dup_rate(BTree(), 1_000, 0.25, (1, 1500)),
                "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000, 0.25, (1, 1500)),
                "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000, 0.25, (1, 1500))
            },
            # "Insert 10000 elements 0.25 duplication rate": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 10_000, 0.25, (1, 100000)),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 10_000, 0.25, (1, 100000)),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 10_000, 0.25, (1, 100000))
            # },
            # "Insert 1000000 elements 0.25 duplication rate": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 1_000_000, 0.25, (1, 1_000_000), 100),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000_000, 0.25, (1, 1_000_000), 100),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000_000, 0.25, (1, 1_000_000), 100)
            # },
            "Insert 1000 elements 0.50 duplication rate": {
                "BTree": self.insert_bench_dup_rate(BTree(), 1_000, 0.50, (1, 1500)),
                "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000, 0.50, (1, 1500)),
                "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000, 0.50, (1, 1500))
            },
            "Insert 1000 elements 0.75 duplication rate": {
                "BTree": self.insert_bench_dup_rate(BTree(), 1_000, 0.75, (1, 1500)),
                "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000, 0.75, (1, 1500)),
                "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000, 0.75, (1, 1500))
            },
        }
        return self.last_run

    def insert_bench_dup_rate(self, tree: BTree, batch_size: int, duplication_rate: float, random_range: tuple, sample_every: int = 1):
        gen = BenchDataGenerator(batch_size, duplication_rate, 0, random_range)

        data1 = gen.generate_random_data()
        times = []

        for i, value in enumerate(data1):
            if i % sample_every == 0:
                times.append(
                    (
                        i,
                        time_call(tree.insert_key, [value])
                    )
                )
            else:
                tree.insert_key(value)

        times = np.array(times)
        return times

    def run_all_and_plot(self, remove_outliers = False, average = False, zscore_upper_limit = 2, averaging_window_size = 5):
        """
        Runs all the tests defined in run_all, or uses cached result if available.
        Plots the results.
        Can filter out outliers and high frequency noise.
        :param remove_outliers: If true a z score test is used to filter out samples with zscore > zscore_upper_limit
        :param average: Apply moving average (low pass filter)
        :param zscore_upper_limit: zscore upper limit
        :param averaging_window_size: Window size for the moving average (higher value => smaller cutoff frequency)
        :return: Results from run_all
        """
        if not self.last_run:
            self.run_all()

        fixtures = self.last_run

        for fixture_title, fixture in fixtures.items():

            for test_title, test_result in fixture.items():

                if remove_outliers:
                    test_result = filter_outliers(test_result, zscore_upper_limit=zscore_upper_limit)
                    test_title = test_title + " (filtered)"

                if average:
                    test_result = moving_average(test_result, window_size=averaging_window_size)
                    test_title = test_title + " (averaged)"

                x = test_result[:, 0]
                y = test_result[:, 1]

                plt.plot(x, y, label=test_title)

            plt.ylabel("seconds")
            plt.xlabel("n. of elements")
            plt.legend()
            plt.title(fixture_title)
            plt.show()

        return fixtures