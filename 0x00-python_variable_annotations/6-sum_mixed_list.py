#!/usr/bin/env python3
""" Sum mixed list module
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ sum int and float mixed items in list and
    return float of total sum
    """

    return sum(mxd_list)
