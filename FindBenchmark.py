import os

import numpy as np

from benchmarking.utils import time_call, time_call_return
from benchmarking.BenchDataGenerator import BenchDataGenerator
from trees.BTree import BTree
from trees.BoolBTree import BoolBTree
from trees.LLBTree import LLBTree
import matplotlib.pyplot as plt


class FindBenchmark:

    def __init__(self):
        self.last_run = {}

    def search_bench(self, tree, values, search_keys, collect = False):
        # Fill the treee
        for value in values:
            tree.insert_key(value)

        # Measure search times
        times = []
        for value in search_keys:
            time, res = time_call_return(tree.find_all, [value], times=5)
            if collect:
                time += time_call(list, [res], times=5)
            times.append(
                time
            )
        return np.average(times), np.std(times)

    def run_benchmark(self, size, duplication_rate, data_range=None):
        gen = BenchDataGenerator(size, duplication_rate, 0, data_range)
        values = gen.generate_random_data()
        search_keys = gen.generate_search_keys(values)
        return {
            "BTree": self.search_bench(BTree(), values, search_keys),
            "BoolBTree": self.search_bench(BoolBTree(), values, search_keys),
            "LLBTree": self.search_bench(LLBTree(), values, search_keys),
            "LLBTree (collect)": self.search_bench(LLBTree(), values, search_keys, collect=True),
        }

    def run_all(self):
        self.last_run["find_all avg time 1000 elements, 0.05 duplication rate"] = self.run_benchmark(1000, 0.05)
        self.last_run["find_all avg time 1000 elements, 0.15 duplication rate"] = self.run_benchmark(1000, 0.15)
        self.last_run["find_all avg time 1000 elements, 0.25 duplication rate"] = self.run_benchmark(1000, 0.25)
        self.last_run["find_all avg time 1000 elements, 0.50 duplication rate"] = self.run_benchmark(1000, 0.50)
        self.last_run["find_all avg time 1000 elements, 0.75 duplication rate"] = self.run_benchmark(1000, 0.75)
        self.last_run["find_all avg time 1000 elements, 0.90 duplication rate"] = self.run_benchmark(1000, 0.90)
        self.last_run["find_all avg time 1000 elements, 0.95 duplication rate"] = self.run_benchmark(1000, 0.95)
        self.last_run["find_all avg time 1000 elements, 0.99 duplication rate"] = self.run_benchmark(1000, 0.99)

        self.last_run["find_all avg time 10000 elements, 0.05 duplication rate"] = self.run_benchmark(10000, 0.05)
        self.last_run["find_all avg time 10000 elements, 0.15 duplication rate"] = self.run_benchmark(10000, 0.15)
        self.last_run["find_all avg time 10000 elements, 0.25 duplication rate"] = self.run_benchmark(10000, 0.25)
        self.last_run["find_all avg time 10000 elements, 0.50 duplication rate"] = self.run_benchmark(10000, 0.50)
        self.last_run["find_all avg time 10000 elements, 0.75 duplication rate"] = self.run_benchmark(10000, 0.75)
        self.last_run["find_all avg time 10000 elements, 0.90 duplication rate"] = self.run_benchmark(10000, 0.90)
        self.last_run["find_all avg time 10000 elements, 0.95 duplication rate"] = self.run_benchmark(10000, 0.95)
        self.last_run["find_all avg time 10000 elements, 0.99 duplication rate"] = self.run_benchmark(10000, 0.99)

    def run_all_and_plot(self, export=""):
        if not self.last_run:
            self.run_all()

        for benchmark_name, data in self.last_run.items():
            print(f"{benchmark_name}: {data}")

            names = list(data.keys())
            avg_times = [item[0] for item in data.values()]
            std_devs = [item[1] for item in data.values()]

            plt.figure(figsize=(8, 6))

            # Bar plot for average times
            plt.bar(names, avg_times, color='skyblue', label="Average Time")

            # Error bars for standard deviation
            plt.errorbar(names, avg_times, yerr=std_devs, fmt='none', capsize=5, color='black', label="Std Dev")

            plt.xlabel("Data Structure")
            plt.ylabel("Runtime (seconds) (average over 5 runs)")
            plt.title(benchmark_name)
            plt.grid(axis='y', linestyle='--')
            plt.legend()
            plt.tight_layout()

            if export:
                os.makedirs(f"plots/{export}", exist_ok=True)
                plt.savefig(f"plots/{export}/{benchmark_name}.png")

            plt.show()