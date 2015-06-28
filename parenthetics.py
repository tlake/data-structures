#!/usr/bin/env python


<<<<<<< HEAD
def parenthetics2(str):
    parens = []
    for item in str:
        parens.append(item)
=======
def parenthetics(str, symbol="()"):
    open_symbol, closed_symbol = symbol
>>>>>>> 4a66c7df490e553fa0100f677fcd45e697c4f4bc
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
<<<<<<< HEAD
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
=======
>>>>>>> 4a66c7df490e553fa0100f677fcd45e697c4f4bc
    else:
        return 0
