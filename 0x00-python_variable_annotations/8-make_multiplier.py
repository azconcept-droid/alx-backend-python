#!/usr/bin/env python3
""" Multiplier module
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier
    """

    def do_multiply(factor: float) -> float:
        """do multiplication"""

        return factor * multiplier

    return do_multiply
