#!/usr/bin/env python3
""" Concurrent coroutines module
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for n times with max_delay
    """
    # delays: list of float
    delays: List[float] = []

    # collect tasks with respect to time to finish
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # collect returned tasks result in ascending other
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
