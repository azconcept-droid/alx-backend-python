#!/usr/bin/env python3
""" Async generator module
"""
import random
import asyncio
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[float, Any]:
    """ Generator function
    """

    for _ in range(10):
        rand_num: float = random.uniform(0, 10)
        yield rand_num
        await asyncio.sleep(1)
