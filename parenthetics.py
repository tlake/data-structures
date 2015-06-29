#!/usr/bin/env python
from __future__ import unicode_literals
from stack import Stack


def parenthetics(string, symbol='()'):
    open_symbol, closed_symbol = symbol
    stack = Stack()
    for char in string:
        if char == open_symbol:
            stack.push(open_symbol)
        if char == closed_symbol:
            if stack.pop() == 0:
                return -1
    if stack.size() > 0:
        return 1
    else:
        return 0
