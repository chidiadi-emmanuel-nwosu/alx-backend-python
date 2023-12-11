#!/usr/bin/env python3
"""2-measure_runtime"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine with a specified
    maximum delay.

    Args:
    - max_delay (int): The maximum delay value for wait_random.

    Returns:
    - asyncio.Task: An asyncio.Task representing the concurrent execution
                    of wait_random with the specified max_delay.
    """
    async def task_wrapper(max_delay):
        return await wait_random(max_delay)

    task = asyncio.create_task(task_wrapper(max_delay))

    return task
