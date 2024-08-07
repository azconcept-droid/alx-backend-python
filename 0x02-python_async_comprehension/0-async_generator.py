#!/usr/bin/env python3
""" Async generator module
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """ Generator function
    """

    for _ in range(10):
        rand_num: float = random.uniform(0, 10)
        yield rand_num
        await asyncio.sleep(1)
