Feature: Sorting lists

  Scenario Outline: Sorting numbers
    Given We have a list of <numbers>
    When We sort them with <algorithm>
    Then It is sorted

    Examples:
      | numbers                                  | algorithm       |
      | [86, 83, 11, 56, 39, 4, 94, 21, 24, 61]  | bubble          |
      | [36, 74, 54, 79, 100, 81, 51, 29, 2, 47] | insertion       |
      | [80, 12, 18, 15, 52, 82, 38, 17, 53, 34] | merge           |
      | [50, 97, 60, 44, 13, 27, 73, 40, 66, 98] | radix           |
      | [31, 46, 26, 5, 28, 20, 33, 90, 85, 78]  | bucket          |
      | [70, 87, 41, 65, 10, 99, 37, 45, 92, 49] | cocktail_shaker |
      | [42, 25, 16, 72, 14, 30, 84, 57, 93, 71] | quick           |
      | [63, 75, 89, 55, 59, 96, 7, 6, 19, 67]   | comb            |
      | [23, 1, 77, 35, 62, 3, 43, 64, 48, 22]   | max_heap        |
      | [68, 9, 58, 91, 88, 32, 76, 69, 95, 8]   | min_heap        |