#!/usr/bin/env python3
"""task 3"""
import time
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    coro = wait_random(max_delay)
    return asyncio.create_task(coro)
