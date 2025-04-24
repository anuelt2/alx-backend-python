#!/usr/bin/env python3
"""Module with sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Type-annotated function that returns sum of list items"""
    return sum(mxd_list)
