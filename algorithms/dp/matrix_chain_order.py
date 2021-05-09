'''
Dynamic Programming
Implementation of matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''

import sys

INF = float("inf")

def matrix_chain_order(array):
    n = len(array)
    # create the table to store solutions to sub problems
    m = [[0 for _ in range(n)] for _ in range(n)]

    # l is the length of the chain
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            # store a maximum integer in the table for further comparison
            m[i][j] = sys.maxsize
            for k in range(i, j):
                # q holds the value of multiplication cost till j elements
                q = m[i][k] + m[k + 1][j] + array[i - 1] * array[k] * array[j]
                # compare previous cost with q
                if q < m[i][j]:
                    m[i][j] = q
    # last element of first row contains the result to the entire problem
    return m[1][n - 1]

