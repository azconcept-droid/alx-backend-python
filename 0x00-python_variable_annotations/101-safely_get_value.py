#!/usr/bin/env python3
""" Safely get value module
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ return the value of dictionary
    else return None
    """
    if key in dct:
        return dct[key]
    else:
        return default
