import random
import timeit

from algorithms.sort import (quick_sort, bubble_sort, gnome_sort, pancake_sort)


def generate_random_list(size):
    filled_list = []
    for _ in range(0, size):
        filled_list.append(random.randint(0, size))
    return filled_list


def benchmark_run(func, list):
    start_time = timeit.default_timer()
    func(list)
    return timeit.default_timer() - start_time


list_of_sample_size = [1000, 10000, 100000, 500000, 1000000]
algorithm_to_benchmark = [quick_sort, bubble_sort, gnome_sort, pancake_sort]
num_runs = 10
duration = 0
for algorithm in algorithm_to_benchmark:
    print("Tested Algorithm: " + algorithm.__name__)
    for n in list_of_sample_size:
        for r in range(0, num_runs):
            duration += benchmark_run(algorithm, generate_random_list(n))
        print("Sample size: " + str(n) + "\n    Number of Runs: " + str(num_runs) + "\n    Avg.Duration: " + str(
            duration / num_runs))
        duration = 0
