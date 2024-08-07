#!/usr/bin/env python3
""" Concurrent coroutines module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for n times with max_delay
    """
    # delays: list of float
    delays: List[float] = []

    # collect tasks with respect to time to finish
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # collect returned tasks in ascending other
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
