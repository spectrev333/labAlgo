from InsertBenchmark import InsertBenchmark
from FindBenchmark import FindBenchmark

test_bench = InsertBenchmark()

test_bench.run_all_and_plot(export="normal")
test_bench.run_all_and_plot(remove_outliers=True, average=True, export="filtered_averaged")
test_bench.run_all_and_plot(remove_outliers=True, average=True, averaging_window_size=50, export="filtered_averaged_50")

find_benchmark = FindBenchmark()

find_benchmark.run_all_and_plot(export="find-normal")
