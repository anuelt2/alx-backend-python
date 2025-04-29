#!/usr/bin/env python3
"""Module with asynchronous coroutine async_comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine using async comprehension over async_generator
    and return the result
    """
    return [num async for num in async_generator()]
