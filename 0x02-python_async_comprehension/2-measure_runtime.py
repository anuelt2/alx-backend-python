#!/usr/bin/env python3
"""Module with asynchronous coroutine measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Asynchronous coroutine that measures and returns total runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
