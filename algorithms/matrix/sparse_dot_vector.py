#! /usr/bin/env python3

"""
Suppose we have very large sparse vectors, which contains a lot of zeros and double .

find a data structure to store them
get the dot product of them
"""


def vector_to_index_value_list(vector):
    return [(i, v) for i, v in enumerate(vector) if v != 0.0]


def dot_product(iv_list1, iv_list2):

    product = 0
    p1 = len(iv_list1) - 1
    p2 = len(iv_list2) - 1

    while p1 >= 0 and p2 >= 0:
        i1, v1 = iv_list1[p1]
        i2, v2 = iv_list2[p2]

        if i1 < i2:
            p1 -= 1
        elif i2 < i1:
            p2 -= 1
        else:
            product += v1 * v2
            p1 -= 1
            p2 -= 1

    return product

