#!/usr/bin/env python


def parenthetics(str):
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
