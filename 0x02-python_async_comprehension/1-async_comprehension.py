#!/usr/bin/env python3
""" Async comprehensions module
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Generate random number using async comprehensions
    """

    return [i async for i in async_generator()]
