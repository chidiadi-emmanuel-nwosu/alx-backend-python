#!/usr/bin/env python3
"""2-measure_runtime.py"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime by executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
    - float: Total runtime in seconds.
    """

    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.time()

    return stop - start
