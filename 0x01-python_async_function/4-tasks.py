#!/usr/bin/env python3
""" Concurrent coroutines module
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for n times with max_delay
    """
    delay: float
    delays: List[float] = []

    index = 0
    while index < n:
        delay = await task_wait_random(max_delay)
        delays.append(delay)
        index += 1

    return delays
