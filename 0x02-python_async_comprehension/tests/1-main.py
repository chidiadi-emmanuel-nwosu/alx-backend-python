#!/usr/bin/env python3

import asyncio
from sys import path

path.append('../')
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
