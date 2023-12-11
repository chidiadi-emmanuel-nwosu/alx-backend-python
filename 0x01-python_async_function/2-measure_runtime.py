#!/usr/bin/env python3
"""2-measure_runtime"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for 'wait_n' function.

    Args:
    - n (int): Number of times to call 'wait_random'.
    - max_delay (int): Maximum delay value for each 'wait_random' call.

    Returns:
    - float: Average time taken per operation in 'wait_n'.
    """
    async def measure(n, max_delay):
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        total_time = end_time - start_time

        return total_time / n if n > 0 else 0

    return asyncio.run(measure(n, max_delay))
