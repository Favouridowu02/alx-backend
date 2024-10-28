#!/usr/bin/env python3
"""
    This Module contains a function `0-simple_helper_function.py`
    The function returns a tuple of the start and end index
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
        This function returns  a tuple of size two containing a start
        index and an end index corresponding to the range of indexes to
        return in a list for those particular pagination parameters.

        Arguments:
            page: The page number
            page_size; The page size

        Return: This function returns a tuple of the start and end index
    """
    start_index = (page-1) * page_size
    end_index = (page * page_size)
    return (start_index, end_index)
