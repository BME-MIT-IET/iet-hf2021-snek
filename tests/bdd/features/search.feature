Feature: Searching in lists

  Scenario Outline: Searching for number's position
    Given We have a list of <numbers>
    When We search for number <number> with <algorithm>
    Then We get index <index>

    Examples:
      | numbers                                       | number | index | algorithm        |
      | [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6] | 1      | 0     | first_occurrence |
      | [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6] | 3      | 3     | first_occurrence |
      | [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6] | 5      | 11    | first_occurrence |
      | [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6] | 7      | None  | first_occurrence |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 3      | 5     | last_occurrence  |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 5      | 10    | last_occurrence  |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 7      | None  | last_occurrence  |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 1      | 0     | last_occurrence  |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 4      | 6     | linear_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 5      | 10    | linear_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | 7      | -1    | linear_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]    | -1     | -1    | linear_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]          | 5      | 10    | binary_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]          | 6      | 11    | binary_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]          | 7      | None  | binary_search    |
      | [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]          | -1     | None  | binary_search    |
