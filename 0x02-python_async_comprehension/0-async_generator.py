#!/usr/bin/env python3
"""Module with asynchronous coroutine async_generator"""

import asyncio
import random


async def async_generator():
    """Asynchronous coroutine that yields a random number for 10 loops"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
