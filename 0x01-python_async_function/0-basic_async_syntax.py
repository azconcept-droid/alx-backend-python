#!/usr/bin/env python3
""" Basic aync module
"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine
    that takes in an integer argument max_delay
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    """

    return random.uniform(0, max_delay)
