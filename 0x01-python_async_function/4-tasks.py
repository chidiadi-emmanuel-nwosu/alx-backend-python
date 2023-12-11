#!/usr/bin/env python3
"""4-tasks.py"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns 'task_wait_random' 'n' times with specified 'max_delay'.

    Args:
    - n (int): The number of times to call 'wait_random'.
    - max_delay (int): The maximum delay value for each 'wait_random' call.

    Returns:
    - List[float]: A list of delays (float values) in ascending order without using 'sort()'.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = []

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays.sort()
    return delays
