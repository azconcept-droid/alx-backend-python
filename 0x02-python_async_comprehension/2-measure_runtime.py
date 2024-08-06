#!/usr/bin/env python3
""" Measure run time Module
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the time it takes for 4 parallel
    calls of async_comprehension function
    """

    total_time: float

    start_time: float = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                   async_comprehension(),  async_comprehension())
    total_time = time.perf_counter() - start_time

    return total_time
