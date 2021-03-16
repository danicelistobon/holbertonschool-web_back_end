#!/usr/bin/env python3
"""Takes a list mxd_lst of ints and floats and returns their sum as a float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum as a float
    """
    return float(sum(mxd_lst))
