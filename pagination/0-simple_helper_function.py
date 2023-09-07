#!/usr/bin/env python3
"""Task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """retrun a tuple with the start and end index of a page"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
