#!/usr/bin/env python

from parenthetics import parenthetics

testText = "12345m67890!@#~`$%^&*/.,;'=-+_[]{}:?<>'"


def test_too_many_open_paren():
    assert parenthetics("(") == 1
    assert parenthetics("((") == 1
    assert parenthetics("(()") == 1
    assert parenthetics("()(") == 1
    assert parenthetics("()()()(") == 1
    assert parenthetics("(adding(text((" + testText + ")works)too)") == 1
    #  -------------
    #  Other symbols
    #  -------------

    #  Square Brackets []
    assert parenthetics("[", "[]") == 1
    assert parenthetics("[[", "[]") == 1
    assert parenthetics("[[]", "[]") == 1
    assert parenthetics("[][", "[]") == 1
    assert parenthetics("[][][][", "[]") == 1
    assert parenthetics("[adding[text[[" + testText + "]works]too]", "[]") == 1

    #  Curly Brackets {}
    assert parenthetics("{", "{}") == 1
    assert parenthetics("{{", "{}") == 1
    assert parenthetics("{{}", "{}") == 1
    assert parenthetics("{}{", "{}") == 1
    assert parenthetics("{}{}{}{", "{}") == 1
    assert parenthetics("{adding{text{{" + testText + "}works}too}", "{}") == 1

    #  Angle Brackets <>
    assert parenthetics("<", "<>") == 1
    assert parenthetics("<<", "<>") == 1
    assert parenthetics("<<<>", "<>") == 1
    assert parenthetics("<<><", "<>") == 1
    assert parenthetics("<<><<><<><", "<>") == 1
    assert parenthetics("<adding<text<<" + testText + "<>works<>too<>", "<>") == 1

    #  Arbitrary Symbols 5m
    assert parenthetics("5", "5m") == 1
    assert parenthetics("55", "5m") == 1
    assert parenthetics("555m", "5m") == 1
    assert parenthetics("55m5", "5m") == 1
    assert parenthetics("55m55m55m5", "5m") == 1
    assert parenthetics("5adding5text55" + testText + "5mworks5mtoo5m", "5m") == 1


def test_too_many_closed_paren():
    assert parenthetics(")") == -1
    assert parenthetics("))") == -1
    assert parenthetics("())") == -1
    assert parenthetics(")()") == -1
    assert parenthetics("))") == -1
    assert parenthetics("(adding(text(" + testText + ")(workstoo))))") == -1
    #  -------------
    #  Other symbols
    #  -------------

    #  Square Brackets []
    assert parenthetics("]", "[]") == -1
    assert parenthetics("]]", "[]") == -1
    assert parenthetics("[]]", "[]") == -1
    assert parenthetics("][]", "[]") == -1
    assert parenthetics("]]", "[]") == -1
    assert parenthetics("[adding[text[" + testText + "][workstoo]]]]", "[]") == -1
    #  Curly Brackets {}
    assert parenthetics("}", "{}") == -1
    assert parenthetics("}}", "{}") == -1
    assert parenthetics("{}}", "{}") == -1
    assert parenthetics("}{}", "{}") == -1
    assert parenthetics("}}", "{}") == -1
    assert parenthetics("{adding{text{" + testText + "}{workstoo}}}}", "{}") == -1
    #  Angle Brackets <>
    assert parenthetics(">", "<>") == -1
    assert parenthetics(">>", "<>") == -1
    assert parenthetics("<>>", "<>") == -1
    assert parenthetics("><>", "<>") == -1
    assert parenthetics(">>", "<>") == -1
    assert parenthetics("<adding<text<" + testText + "><workstoo>>>>", "<>") == -1
    #  Arbitrary Symbols 5m
    assert parenthetics("m", "5m") == -1
    assert parenthetics("mm", "5m") == -1
    assert parenthetics("5mm", "5m") == -1
    assert parenthetics("m5m", "5m") == -1
    assert parenthetics("mm", "5m") == -1
    assert parenthetics("5adding5text5" + testText + "m5workstoommmm", "5m") == -1


def test_correct_paren():
    assert parenthetics("()") == 0
    assert parenthetics("()()") == 0
    assert parenthetics("(())") == 0
    assert parenthetics("(adding(text(" + testText + ")works)too)") == 0
    #  -------------
    #  Other symbols
    #  -------------

    #  Square Brackets []
    assert parenthetics("[]", "[]") == 0
    assert parenthetics("[][]", "[]") == 0
    assert parenthetics("[[]]", "[]") == 0
    assert parenthetics("[adding[text[" + testText + "]works]too]", "[]") == 0
    #  Curly Brackets {}
    assert parenthetics("{}", "{}") == 0
    assert parenthetics("{}{}", "{}") == 0
    assert parenthetics("{{}}", "{}") == 0
    assert parenthetics("{adding{text{" + testText + "}works}too}", "{}") == 0
    #  Angle Brackets <>
    assert parenthetics("<>", "<>") == 0
    assert parenthetics("<><>", "<>") == 0
    assert parenthetics("<<>>", "<>") == 0
    assert parenthetics("<adding<text<" + testText + ">works>too>", "<>") == 0
    #  Arbitrary Symbols 5m
    assert parenthetics("5m", "5m") == 0
    assert parenthetics("5m5m", "5m") == 0
    assert parenthetics("55mm", "5m") == 0
    assert parenthetics("5adding5text5" + testText + "mworksmtoom", "5m") == 0
