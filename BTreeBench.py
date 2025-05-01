from BoolBTree import BoolBTree
from LLBTree import LLBTree
from TestBench import TestBench
from TestDataGenerator import TestDataGenerator
from BTree import BTree
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore

class BTreeBench(TestBench):

    def __init__(self, tree):
        super()
        self.tree = tree
        self.last_run = None

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
            # "Insert 1000 elements 0.25 duplication rate": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 1_000, 0.25, (1, 1500)),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000, 0.25, (1, 1500)),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000, 0.25, (1, 1500))
            # },
            "Insert 10000 elements 0.25 duplication rate": {
                "BTree": self.insert_bench_dup_rate(BTree(), 10_000, 0.25, (1, 100000)),
                "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 10_000, 0.25, (1, 100000)),
                "LLBTree": self.insert_bench_dup_rate(LLBTree(), 10_000, 0.25, (1, 100000))
            },
            # "Insert 1000000 elements 0.25 duplication rate": {
            #     "BTree": self.insert_bench_dup_rate(BTree(), 1_000_000, 0.25, (1, 1_000_000), 100),
            #     "BoolBTree": self.insert_bench_dup_rate(BoolBTree(), 1_000_000, 0.25, (1, 1_000_000), 100),
            #     "LLBTree": self.insert_bench_dup_rate(LLBTree(), 1_000_000, 0.25, (1, 1_000_000), 100)
            # },
        }
        return self.last_run

    def insert_bench_dup_rate(self, tree: BTree, batch_size: int, duplication_rate: float, random_range: tuple, sample_every: int = 1):
        gen = TestDataGenerator(batch_size, duplication_rate, 0, random_range)

        data1 = gen.generate_random_data()
        times = []

        for i, value in enumerate(data1):
            if i % sample_every == 0:
                times.append(
                    (
                        i,
                        TestBench.time_call(tree.insert_key, [value])
                    )
                )
            else:
                tree.insert_key(value)

        times = np.array(times)
        return times

    def run_all_and_plot(self):
        if not self.last_run:
            self.run_all()

        fixtures = self.last_run

        for fixture_title, fixture in fixtures.items():

            for test_title, test_result in fixture.items():

                x = test_result[:, 0]
                y = test_result[:, 1]

                # if filter_outliers:
                #     z_scores = zscore(y)
                #     mask = np.abs(z_scores) < 2
                #     test_result = test_result[mask]
                #     x = test_result[:, 0]
                #     y = test_result[:, 1]

                plt.plot(x, y, label=test_title)

            plt.legend()
            plt.title(fixture_title)
            plt.show()

        return fixtures

    def export_to_csv(self):
        # if not self.last_run:
        #     self.run_all()
        raise NotImplemented()