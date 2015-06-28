#!/usr/bin/env python
from __future__ import unicode_literals


def parenthetics(str, symbol='()'):
    print "d"
    open_symbol, closed_symbol = symbol
    open_count, closed_count = 0, 0
    for char in str:
        if char == open_symbol:
            open_count += 1
        elif char == closed_symbol:
            closed_count += 1
        if open_count < closed_count:
            return -1
    if open_count > closed_count:
        return 1
    else:
        return 0
