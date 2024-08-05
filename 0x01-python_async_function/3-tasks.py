#!/usr/bin/env python3
""" Asyncio task module
"""
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    """Create task and
    return asyncio.task for wait_random function
    """

    # Schedule wait_random() to run soon concurrently
    # with "task_wait_random".
    task = asyncio.create_task(wait_random(max_delay))

    return task
