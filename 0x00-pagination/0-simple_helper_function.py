#!/usr/bin/env python3
"""Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """Range for pagination
    """
    return (page * page_size - page_size, page_size * page)
