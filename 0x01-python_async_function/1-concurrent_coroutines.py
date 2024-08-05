#!/usr/bin/env python3
""" Concurrent coroutines module
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for n times with max_delay
    """
    delay: float
    delays: List[float] = []

    index = 0
    while index < n:
        delay = await wait_random(max_delay)
        delays.append(delay)
        index +=1

    return delays
