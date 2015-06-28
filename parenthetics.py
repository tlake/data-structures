#!/usr/bin/env python


def parenthetics(str, symbol="()"):
    open_symbol, closed_symbol = symbol
    count = 0
    for item in str:
        if item == open_symbol:
            count += 1
        elif item == closed_symbol:
            count -= 1
    if count < 0:
        return -1
    if count > 0:
        return 1
    else:
        return 0
