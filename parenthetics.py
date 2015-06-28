#!/usr/bin/env python


def parenthetics(str, symbol='()'):
    count = 0
    open_symbol, closed_symbol = symbol
    for item in str:
        if item == "open_symbol":
            count += 1
        elif item == "closed_symbol":
            count -= 1
        if count == -1:
            return count
    if count == 0:
        return count
    if count > 0:
        return 1
