#!/usr/bin/env python3
"""Module with safe_first_element function"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type-annotated function that returns the first sequence item"""
    if lst:
        return lst[0]
    else:
        return None
