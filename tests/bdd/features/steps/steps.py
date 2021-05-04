from behave import given, use_step_matcher, when, then

from algorithms.search import (
    binary_search,
    first_occurrence,
    last_occurrence,
    linear_search,
)
from algorithms.sort import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    radix_sort,
    bucket_sort,
    cocktail_shaker_sort,
    quick_sort,
    comb_sort,
    max_heap_sort,
    min_heap_sort
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
    "min_heap": min_heap_sort,
    "first_occurrence": first_occurrence,
    "last_occurrence": last_occurrence,
    "linear_search": linear_search,
    "binary_search": binary_search
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


def initialize_algorithm(context, algorithm):
    """
    Helper function to initialize the context with the given algorithm
    :param algorithm: The algorithm to set on the context
    :param context: The context of the testcase
    """
    context.algorithm = algorithms[algorithm]
    assert context.algorithm is not None
    return context.algorithm


@given("We have a list of (?P<numbers>.+)")
def step_impl(context, numbers):
    """
    Step to load the unsorted array into context. Using eval, because the test data can be trusted.
    :param numbers: Array to check if sorted
    :param context: The context of the testcase
    """
    context.numbers = eval(numbers)


@when("We sort them with (?P<algorithm>.+)")
def step_impl(context, algorithm):
    """
    Step to lookup the tested algorithm, and perform it on the unsorted_numbers array.
    :param algorithm: The algorithm which we test
    :param context: The context of the testcase
    """
    initialize_algorithm(context, algorithm)
    context.sorted_numbers = context.algorithm(context.numbers)


@then("It is sorted")
def step_impl(context):
    """
    Step to check if the array was sorted properly or not
    :param context: The context of the testcase
    """
    assert is_sorted(context.sorted_numbers)
    print(context.sorted_numbers)


@when("We search for number (?P<number>.+) with (?P<algorithm>.+)")
def step_impl(context, number, algorithm):
    """
    Step to execute the supplied algorithm. Using eval, because the test data can be trusted.
    :param algorithm: The algorithm to use
    :param number: The number we are looking for
    :param context: The context of the testcase
    """
    initialize_algorithm(context, algorithm)
    context.found_index = context.algorithm(context.numbers, eval(number))


@then("We get index (?P<index>.+)")
def step_impl(context, index):
    """
    Step to check if the algorithm returned with the right index
    :param index: The expected index
    :param context: The context of the testcase
    """
    assert context.found_index == eval(index)
