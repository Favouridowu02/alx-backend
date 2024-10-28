#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

# My written test cases
res = index_range(0, 8)
print(type(res))
print(res)


res = index_range()
print(type(res))
print(res)

res = index_range(1, -1)
print(type(res))
print(res)

res = index_range(1, 8)
print(type(res))
print(res)
