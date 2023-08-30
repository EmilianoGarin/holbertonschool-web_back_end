#!/usr/bin/env python3
"""task 0"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """task 1"""
    return [x async for x in async_generator()]
