#!/usr/bin/env python3
"""Module with asynchronous coroutine async_comprehension"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Asynchronous coroutine using async comprehension over async_generator
    and return the result
    """
    return [i async for i in async_generator()]
