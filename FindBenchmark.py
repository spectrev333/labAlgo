import csv
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

    def find_all_bench(self, tree, values, search_keys, collect = False):
        """
        Perform a find_all benchmark
        :param tree: Benchmark subject
        :param values: Values to fill the tree before benchmarking
        :param search_keys: Subset of values to search
        :param collect: If true then a list collection is applied to the return value of find_all
        :return: A tuple containing respectively: average find time, standard deviation
        """
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
        return times

    def find_bench(self, tree, values, search_keys):
        """
        Perform a find benchmark
        :param tree: Benchmark subject
        :param values: Values to fill the tree before benchmarking
        :param search_keys: Subset of values to search
        :return: A tuple containing respectively: average find time, standard deviation
        """
        # Fill the treee
        for value in values:
            tree.insert_key(value)

        # Measure search times
        times = []
        for value in search_keys:
            time, res = time_call_return(tree.find, [value], times=5)
            times.append(
                time
            )
        return times

    def run_benchmark(self, size, duplication_rate, data_range=None):
        """
        Run benchmark generating a dataset first.
        :param size: Size of the dataset
        :param duplication_rate: dataset duplication rate
        :param data_range: leave None, trust me
        """
        print(f"Benchmarking find_all... ({size} elements, {duplication_rate} dup. rate)")
        gen = BenchDataGenerator(size, duplication_rate, 0, data_range)
        values = gen.generate_random_data()
        search_keys = gen.generate_search_keys(values)
        self.last_run["find_all avg time %d elements, %.2f dup. rate" % (size, duplication_rate)] =  {
            "BTree": self.find_all_bench(BTree(), values, search_keys),
            "BoolBTree": self.find_all_bench(BoolBTree(), values, search_keys),
            "LLBTree": self.find_all_bench(LLBTree(), values, search_keys),
            "LLBTree (collect)": self.find_all_bench(LLBTree(), values, search_keys, collect=True),
        }
        # self.last_run["find avg time %d elements, %.2f dup. rate" % (size, duplication_rate)] = {
        #     "BTree": self.find_bench(BTree(), values, [-1, -2, -3]),
        #     "BoolBTree": self.find_bench(BoolBTree(), values, [-1, -2, -3]),
        #     "LLBTree": self.find_bench(LLBTree(), values, [-1, -2, -3]),
        # }

    def run_all(self):
        """
        Run all benchmark cases
        """
        self.run_benchmark(1000, 0.05)
        self.run_benchmark(1000, 0.15)
        self.run_benchmark(1000, 0.25)
        self.run_benchmark(1000, 0.50)
        self.run_benchmark(1000, 0.75)
        self.run_benchmark(1000, 0.90)
        self.run_benchmark(1000, 0.95)
        self.run_benchmark(1000, 0.99)

        self.run_benchmark(10000, 0.05)
        self.run_benchmark(10000, 0.15)
        self.run_benchmark(10000, 0.25)
        self.run_benchmark(10000, 0.50)
        self.run_benchmark(10000, 0.75)
        self.run_benchmark(10000, 0.90)
        self.run_benchmark(10000, 0.95)
        self.run_benchmark(10000, 0.99)

    def run_all_and_plot(self, export=""):
        """
        Visualize benchmark results
        :param export: Directory under "plots/" where data should be exported
        """
        if not self.last_run:
            self.run_all()

        # Initialize csv export
        all_data = [] if export else None
        header = ["Benchmark", "Data Structure", "Average Time", "Standard Deviation"]

        for benchmark_name, data in self.last_run.items():
            # print(f"{benchmark_name}: {data}")

            names = list(data.keys()) # Data structure name
            times = data.values() # Times array

            if export:
                for name, time_array in zip(names, times):
                    all_data.append([benchmark_name, name, np.average(time_array), np.std(time_array)])

            # Bar plot with y error
            plt.figure(figsize=(8, 6))
            plt.boxplot(times, labels=names, showfliers=False, patch_artist=True, boxprops=dict(facecolor='skyblue'), medianprops=dict(color='black'))
            plt.xlabel("Data Structure")
            plt.ylabel("Runtime (seconds) (average over 5 runs)")
            plt.title(benchmark_name)
            plt.grid(axis='y', linestyle='--')
            plt.tight_layout()

            # Save benchmark plot
            if export:
                os.makedirs(f"plots/{export}", exist_ok=True)
                plt.savefig(f"plots/{export}/{benchmark_name}.png")
                print(f"plot saved at plots/{export}/{benchmark_name}.png")

            plt.show()

        # Save everything in a csv
        if export:
            with open(f"plots/{export}/benchmarks.csv", 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([header] + all_data)
            print(f"Benchmark data exported to: plots/{export}/benchmarks.csv")
