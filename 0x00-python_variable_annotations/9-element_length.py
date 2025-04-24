#!/usr/bin/env python3
"""Module with element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function that returns length of each list item"""
    return [(i, len(i)) for i in lst]
