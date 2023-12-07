#!/usr/bin/env python3
"""9-element_length.py"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a tuple"""
    return [(i, len(i)) for i in lst]
