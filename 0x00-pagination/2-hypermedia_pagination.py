#!/usr/bin/env python3
"""
    This module contains a function index_range and a class Server
"""
from typing import Tuple, List, Dict
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
        """
            This is the class initialization
        """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            This function returns thst a dictioonary containing tne following

            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer

            Arguments:
                page: the current page number
                page_size: the page size
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        index = index_range(page, page_size)
        new_dict = {
                "page_size": len(self.get_page(page, page_size)),
                "page": page,
                "data": self.get_page(page, page_size),
                "next_page": page + 1 if index[0] < len(self.__dataset) else None,
                "prev_page": page - 1 if index[1] > 2 else None,
                "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
        return new_dict
