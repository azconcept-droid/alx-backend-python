#!/usr/bin/env python3
""" Module that annotate a given function 
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return item and length of the item in tuple
    """
    return [(i, len(i)) for i in lst]