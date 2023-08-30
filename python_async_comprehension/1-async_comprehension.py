#!/usr/bin/env python3
"""task 0"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """task 1"""
    ret = []
    async for x in async_generator():
        ret.append(x)
    return ret