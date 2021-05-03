from behave import *

from algorithms.sort import (
    bubble_sort, insertion_sort, merge_sort, radix_sort, bucket_sort, cocktail_shaker_sort, quick_sort, comb_sort,
    max_heap_sort, min_heap_sort
)

use_step_matcher("re")

algorithms = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
    "cocktail_shaker": cocktail_shaker_sort,
    "quick": quick_sort,
    "comb": comb_sort,
    "max_heap": max_heap_sort,
    "min_heap": min_heap_sort
}


def is_sorted(array):
    """
    Helper function to check if the given array is sorted.
    :param array: Array to check if sorted
    :return: True if sorted in ascending order, else False
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


@given("We have a list of (?P<numbers>.+)")
def step_impl(context, numbers):
    """
    Step to load the unsorted array into context. Using eval, because the test data can be trusted.
    :param numbers: Array to check if sorted
    :param context: The context of the testcase
    """
    context.unsorted_numbers = eval(numbers)


@when("We sort them with (?P<algorithm>.+)")
def step_impl(context, algorithm):
    """
    Step to lookup the tested algorithm, and perform it on the unsorted_numbers array.
    :param algorithm: The algorithm which we test
    :param context: The context of the testcase
    """
    context.algorithm = algorithms[algorithm]
    assert context.algorithm is not None
    context.sorted_numbers = context.algorithm(context.unsorted_numbers)


@then("It is sorted")
def step_impl(context):
    """
    Step to check if the array was sorted properly or not.
    :param context: The context of the testcase
    """
    assert is_sorted(context.sorted_numbers)
    print(context.sorted_numbers)