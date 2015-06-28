#!/usr/bin/env python

from parenthetics import parenthetics


def test_parenthetics():
    assert parenthetics("(()") == 1
    assert parenthetics("()") == 0
    assert parenthetics(")()") == -1
