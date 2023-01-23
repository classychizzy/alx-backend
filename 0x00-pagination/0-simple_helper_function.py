#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """The function returns a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    data = page_size * page
    start_index = data - page_size
    end_index = data
    return (start_index, end_index)
