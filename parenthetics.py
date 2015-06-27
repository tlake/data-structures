#!/usr/bin/env python


def parenthetics2(str):
    parens = []
    for item in str:
        parens.append(item)
    count = 0
    open_parens = []
    for item in str:
        count += 1
        if item == "(":
            open_parens.append(count)
    count_two = 0
    closed_parens = []
    for item in str:
        count_two += 1
        if item == ")":
            closed_parens.append(count_two)
    if len(closed_parens) < len(open_parens):
        return 1
    count_final = 0
    for number in range(len(open_parens) + 1):
        if open_parens[count_final] > closed_parens[count_final]:
            return -1
            break
        count += 1
    return 0


def parenthetics(str, symbol='()'):
    #  Tyler testing a shorter way
    #  We could also have two optional arguments,
    #  but I like this.
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
