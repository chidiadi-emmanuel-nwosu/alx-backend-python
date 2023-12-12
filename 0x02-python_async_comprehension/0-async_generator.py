#!/usr/bin/env python3
"""0-async_generator.py"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous coroutine that yields random numbers between
    0 and 10 after waiting for 1 second asynchronously.

    Yields:
    - float: Random numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
