#!/usr/bin/env python3
"""Task 1"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexs = index_range(page, page_size)
        start = indexs[0]
        end = indexs[1]
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> tuple:
    """retrun a tuple with the start and end index of a page"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
