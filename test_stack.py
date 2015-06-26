#!/usr/bin/env python


from stack import Stack
import pytest


def test_pop():
    assert Stack([1, 2, 3]).pop() == 3


def test_pop_2():
    assert Stack([1]).pop() == 1


def test_push():
    test_stack = Stack([1, 2, 3])
    test_stack.push(4)
    assert test_stack.group.head.val == 4


def test_push_2():
    test_stack = Stack([])
    test_stack.push(1)
    assert test_stack.group.head.val == 1


def test_none():
    test_stack = Stack()
    test_stack.push(2)
    assert test_stack.group.head.val == 2


def test_pop_3():
    with pytest.raises(AttributeError):
        test_stack = Stack()
        test_stack.pop()
