import unittest

from algorithms.stack import first_is_consecutive, second_is_consecutive


class TestConsecutiveStack(unittest.TestCase):

    one_element_is_always_consecutive = [24]
    one_element_is_always_consecutive_2 = [24]
    consecutive_stack = [1, 2, 3, 4, 5, 6]
    consecutive_stack_2 = [1, 2, 3, 4, 5, 6]
    non_consecutive_stack = [1, 2, 3, 4, 6]
    non_consecutive_stack_2 = [1, 2, 3, 4, 6]

    # the algorithm used modifies the input array for some reason

    def test_algo1_one_element(self):
        self.assertTrue(first_is_consecutive(self.one_element_is_always_consecutive))

    def test_algo2_one_element(self):
        self.assertTrue(second_is_consecutive(self.one_element_is_always_consecutive_2))

    def test_algo1_valid(self):
        self.assertTrue(first_is_consecutive(self.consecutive_stack))

    def test_algo2_valid(self):
        self.assertTrue(second_is_consecutive(self.consecutive_stack_2))

    def test_algo1_invalid(self):
        self.assertFalse(first_is_consecutive(self.non_consecutive_stack))

    def test_algo2_invalid(self):
        self.assertFalse(second_is_consecutive(self.non_consecutive_stack_2))
