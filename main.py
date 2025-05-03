from trees.LLBTree import LLBTree

from InsertBenchmark import InsertBenchmark

tree = LLBTree()

test_bench = InsertBenchmark(tree)

test_bench.run_all_and_plot(remove_outliers=True, average=True)
test_bench.run_all_and_plot(remove_outliers=True, average=True, averaging_window_size=50)


