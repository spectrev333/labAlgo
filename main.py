from InsertBenchmark import InsertBenchmark
from FindBenchmark import FindBenchmark

# insert_bench = InsertBenchmark()
#
# insert_bench.run_all_and_plot(export="normal")
# insert_bench.run_all_and_plot(remove_outliers=True, average=True, export="filtered_averaged")

find_benchmark = FindBenchmark()

find_benchmark.run_all_and_plot(export="find-results")
