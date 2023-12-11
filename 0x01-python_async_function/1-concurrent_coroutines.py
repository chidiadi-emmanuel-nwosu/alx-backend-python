#!/usr/bin/env python3
"""1-concurrent_coroutines"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns 'wait_random' 'n' times with specified 'max_delay'.

    Args:
    - n (int): The number of times to call 'wait_random'.
    - max_delay (int): The maximum delay value for each 'wait_random' call.

    Returns:
    - List[float]: A list of delays (float values) in ascending order
                   without using 'sort()'.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = []

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
