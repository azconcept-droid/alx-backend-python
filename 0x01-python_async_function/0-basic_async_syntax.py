#!/usr/bin/env python3
""" Basic aync module
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine
    that takes in an integer argument max_delay
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    """

    # Generate delay time in seconds
    delay: float = random.uniform(0, max_delay)

    # Wait for generated delay time
    await asyncio.sleep(delay)

    # return delay time
    return delay
