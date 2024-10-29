#!/usr/bin/env python3
"""
    This module contains a function index_range and a class Server
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int = 0, page_size: int = 0) -> Tuple[int, int]:
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
        """
            This Function returns the page start_index and end_index

            Arguments:
                page (int): The current page number (1-based).
                page_size (int): The number of items per page.

            Returns:
                List[List]: A list of rows corresponding to the requested page.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        data = self.dataset()

        if (index[0] >= len(data)):
            return []

        return data[index[0]:index[1]]
