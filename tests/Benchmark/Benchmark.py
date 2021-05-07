import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from algorithms.sort import (quick_sort, merge_sort,pigeonhole_sort,counting_sort,radix_sort)


def generate_random_list(size):
    filled_list = []
    for _ in range(0, size):
        filled_list.append(random.randint(0, size))
    return filled_list


def benchmark_run(func, list):
    start_time = timeit.default_timer()
    func(list)
    return timeit.default_timer() - start_time

def plot_maker(list_of_sample_size,algorithm_to_benchmark,name):
    num_runs = 10
    duration = 0
    benchmark_row = []
    for algorithm in algorithm_to_benchmark:
        print(algorithm.__name__)
        for n in list_of_sample_size:
            for _ in range(0, num_runs):
                duration += benchmark_run(algorithm, generate_random_list(n))
            benchmark_row.append([algorithm.__name__, n, (duration / num_runs)])
            duration = 0
    df = pd.DataFrame(data=benchmark_row, columns=["Name", "Sample_size", "Duration"])
    sns.set_theme()
    plt.figure(figsize=(22, 13))
    sns.lineplot(data=df, x="Sample_size", y="Duration", hue="Name", marker="o")
    plt.xticks(list_of_sample_size)
    plt.savefig('Benchmark/Plots/'+name)
    plt.show()

list_of_sample_size = [1000,5000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,125000,150000]
algorithm_to_benchmark = [merge_sort,quick_sort,pigeonhole_sort,counting_sort,radix_sort]
plot_maker(list_of_sample_size,algorithm_to_benchmark,'fast_algo_runs.png')
