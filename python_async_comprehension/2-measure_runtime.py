#!/usr/bin/env python3
"""task 2"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """task 2"""
    tasks = [async_comprehension() for _ in range(4)]
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
