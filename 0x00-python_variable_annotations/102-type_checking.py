#!/usr/bin/env python3
""" Zoom array module
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ repeat item in tuple with respect to the factor

    input: array = (12, 72, 91), factor = 2
    output: [12, 12, 72, 72, 91, 91]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
