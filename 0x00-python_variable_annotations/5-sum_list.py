#!/usr/bin/env python3
""" Sum list module
"""


def sum_list(input_list: list[float]) -> float:
    """ sum float items in list and
    return float of total sum
    """

    # Initialize the total sum
    summ: float = 0.0

    # Add up all items in list
    for item in input_list:
        summ += item

    return summ
