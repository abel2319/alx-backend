#!/usr/bin/env python3
"""Simple pagination
"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """Range for pagination
    """
    return (page * page_size - page_size, page_size * page)


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
        """get data for page
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        data = self.dataset()

        if indexes[0] >= len(data):
            return []

        return data[indexes[0]: min(indexes[1], len(data))]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get data for page
        """ 
        indexes = index_range(page, page_size)
        data = self.get_page(page, page_size)
        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': page + 1 if indexes[1] < len(self.dataset()) else None,
                'prev_page': page - 1 if indexes[0] > 0 else None,
                'total_pages': math.ceil(len(self.dataset()) / page_size)
                }
