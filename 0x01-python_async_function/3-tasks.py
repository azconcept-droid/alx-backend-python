#!/usr/bin/env python3
""" Asyncio task module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create task and
    return asyncio.task for wait_random function
    """

    # Schedule wait_random() to run soon concurrently
    task = asyncio.create_task(wait_random(max_delay))

    return task
