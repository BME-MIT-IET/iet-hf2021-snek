from algorithms.strings import is_valid_coordinates_0, is_valid_coordinates_1, is_valid_coordinates_regular_expression
import unittest


class TestValidateCoordinates(unittest.TestCase):
    valid_format_string1 = "-89.999, 31.324"
    valid_format_string2 = "89.999, 31.324"
    valid_format_string3 = "34.234, 179.99"
    valid_format_string4 = "34.234, -179.99"
    valid_format_string5 = "0.234, -0.2532"

    wrong_format_string = "asdgrt, 3gdfgthfdv"

    out_of_bounds_string1 = "91, 179"
    out_of_bounds_string2 = "-91, 179"
    out_of_bounds_string3 = "23, 181"
    out_of_bounds_string4 = "23, -181"

    out_of_bounds_floating_string1 = "89.234, 180.234"
    out_of_bounds_floating_string2 = "89.234, -180.234"
    out_of_bounds_floating_string3 = "90.234, 175.32"
    out_of_bounds_floating_string4 = "-90.123, 123.234"

    def test_valid_algo0(self):
        self.assertTrue(is_valid_coordinates_0(self.valid_format_string1))
        self.assertTrue(is_valid_coordinates_0(self.valid_format_string2))
        self.assertTrue(is_valid_coordinates_0(self.valid_format_string3))
        self.assertTrue(is_valid_coordinates_0(self.valid_format_string4))
        self.assertTrue(is_valid_coordinates_0(self.valid_format_string5))

    def test_valid_algo1(self):
        self.assertTrue(is_valid_coordinates_1(self.valid_format_string1))
        self.assertTrue(is_valid_coordinates_1(self.valid_format_string2))
        self.assertTrue(is_valid_coordinates_1(self.valid_format_string3))
        self.assertTrue(is_valid_coordinates_1(self.valid_format_string4))
        self.assertTrue(is_valid_coordinates_1(self.valid_format_string5))

    def test_valid_regex(self):
        self.assertTrue(is_valid_coordinates_regular_expression(self.valid_format_string1))
        self.assertTrue(is_valid_coordinates_regular_expression(self.valid_format_string2))
        self.assertTrue(is_valid_coordinates_regular_expression(self.valid_format_string3))
        self.assertTrue(is_valid_coordinates_regular_expression(self.valid_format_string4))
        self.assertTrue(is_valid_coordinates_regular_expression(self.valid_format_string5))

    def test_wrong_format_algo0(self):
        self.assertFalse(is_valid_coordinates_0(self.wrong_format_string))

    def test_wrong_format_algo1(self):
        self.assertFalse(is_valid_coordinates_1(self.wrong_format_string))

    def test_wrong_format_regex(self):
        self.assertFalse(is_valid_coordinates_regular_expression(self.wrong_format_string))

    def test_out_of_bounds_algo0(self):
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_string1))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_string2))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_string3))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_string4))

    def test_out_of_bounds_algo1(self):
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_string1))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_string2))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_string3))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_string4))


    # bug found! regex doesn't work properly
    def test_out_of_bounds_regex(self):
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_string1))
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_string2))
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_string3))
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_string4))

    def test_out_of_bounds_floating_algo0(self):
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_floating_string1))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_floating_string2))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_floating_string3))
        self.assertFalse(is_valid_coordinates_0(self.out_of_bounds_floating_string4))

    def test_out_of_bounds_floating_algo1(self):
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_floating_string1))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_floating_string2))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_floating_string3))
        self.assertFalse(is_valid_coordinates_1(self.out_of_bounds_floating_string4))

    # bug found! regex doesn't work properly
    def test_out_of_bounds_floating_regex(self):
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_floating_string1))
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_floating_string2))
        # this one fails, bc the regex is bad!
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_floating_string3))
        self.assertFalse(is_valid_coordinates_regular_expression(self.out_of_bounds_floating_string4))
