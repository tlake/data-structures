#!/usr/bin/env python
from __future__ import unicode_literals
from parenthetics import parenthetics

testText = "12345m67890!@#~`$%^&*/.,;'=-+_[]{}:?<>'"
testSymbols = ['()', '{}', '[]', '<>', '5m']


def test_extra_open():
    for d in testSymbols:
        o, c = d
        assert parenthetics("{}".format(o), d) == 1
        assert parenthetics("{}{}".format(o, o), d) == 1
        assert parenthetics("{}{}{}".format(o, o, c), d) == 1
        assert parenthetics("{}{}{}".format(o, c, o), d) == 1
        assert parenthetics("{}{}{}{}{}{}{}".format(
                            o, c, o, c, o, c, o), d) == 1
        assert parenthetics("{}adding{}text{}{}".format(
                            o, o, o, o) + testText + "{}works{}too{}".format(
                            c, c, c), d) == 1


def test_extra_closed():
    for d in testSymbols:
        o, c = d
        assert parenthetics("{}".format(c), d) == -1
        assert parenthetics("{}{}".format(c, c), d) == -1
        assert parenthetics("{}{}{}".format(o, c, c), d) == -1
        assert parenthetics("{}{}{}".format(c, o, c), d) == -1
        assert parenthetics("{}{}{}{}{}{}{}".format(
                            o, c, o, c, o, c, c), d) == -1
        assert parenthetics("{}adding{}text{}{}".format(
                            o, o, o, c) + testText + "{}works{}too{}".format(
                            c, c, c), d) == -1


def test_no_extra():
    for d in testSymbols:
        o, c = d
        assert parenthetics("{}{}".format(o, c), d) == 0
        assert parenthetics("{}{}{}{}".format(o, c, o, c), d) == 0
        assert parenthetics("{}{}{}{}".format(o, o, c, c), d) == 0
        assert parenthetics("{}adding{}text{}{}".format(
                            o, o, o, o) + testText + "{}works{}too{}{}".format(
                            c, c, c, c), d) == 0
