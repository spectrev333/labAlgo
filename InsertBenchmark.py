import os
from readline import insert_text

from matplotlib.pyplot import title

from trees.BoolBTree import BoolBTree
from trees.LLBTree import LLBTree
from benchmarking.utils import time_call
from benchmarking.BenchDataGenerator import BenchDataGenerator
from trees.BTree import BTree
import matplotlib.pyplot as plt
import numpy as np
from timeseries import Timeseries, filter_outliers, moving_average


class InsertBenchmark:
    def __init__(self):
        super()
        self.last_run = {}
        self.values = None

    def run_benchmark(self, size, duplication_rate, sample_every=1, data_range=None):
        print(f"Benchmarking insert... ({size} elements, {duplication_rate} dup. rate)")
        gen = BenchDataGenerator(size, duplication_rate, 0, data_range)
        self.values = gen.generate_random_data()
        self.last_run["Insert %d elements, %.2f dup. rate" % (size, duplication_rate)] = {
            "BTree": self.insert_bench(BTree(), sample_every),
            "BoolBTree": self.insert_bench(BoolBTree(), sample_every),
            "LLBTree": self.insert_bench(LLBTree(), sample_every)
        }

    def run_all(self):
        self.run_benchmark(1_000, 0.25)
        self.run_benchmark(1_000, 0.50)
        self.run_benchmark(1_000, 0.75)
        self.run_benchmark(1_000, 0.90)
        self.run_benchmark(1_000, 0.99)
        self.run_benchmark(1_000, 1.0)
        self.run_benchmark(10_000, 0.95)
        self.run_benchmark(10_000, 0.99)
        self.run_benchmark(10_000, 0.999)
        self.run_benchmark(10_000, 1.0)
        # self.run_benchmark(1_000_000, 0.95, sample_every=100)
        # self.run_benchmark(1_000_000, 0.99, sample_every=100)
        return self.last_run

    def insert_bench(self, tree, sample_every: int = 1):
        times = []

        for i, value in enumerate(self.values):
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

    def run_all_and_plot(self, remove_outliers=False, average=False, zscore_upper_limit=2, averaging_window_size=5,
                         export=""):
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

                if average:
                    test_result = moving_average(test_result, window_size=averaging_window_size)

                x = test_result[:, 0]
                y = test_result[:, 1]

                plt.plot(x, y, label=test_title)

            title = f"{fixture_title}"
            title += " filtered" if remove_outliers else ""
            title += f" averaged({averaging_window_size})" if average else ""
            plt.ylabel("Runtime (seconds)")
            plt.xlabel("Nr. of elements")
            plt.legend()
            plt.title(title)

            if export:
                os.makedirs(f"plots/{export}", exist_ok=True)
                np.savetxt(f"plots/{export}/{fixture_title}.csv", test_result, delimiter=",", header="x,y", comments='')
                plt.savefig(f"plots/{export}/{fixture_title}.png")

            plt.show()

        return fixtures
