#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from data_structures.stack import Stack


@pytest.fixture()
def create_stack():
    return Stack([1, 2, 3])


@pytest.fixture()
def create_empty_stack():
    return Stack()


@pytest.fixture
def create_single_item_stack():
    return Stack([1])


def test_pop(create_stack):
    assert create_stack.pop() == 3


def test_pop_2(create_single_item_stack):
    assert create_single_item_stack.pop() == 1


def test_push(create_stack):
    test_stack = create_stack
    test_stack.push(4)
    assert test_stack.group.head.val == 4


def test_push_to_empty_stack(create_empty_stack):
    test_stack = create_empty_stack
    test_stack.push(1)
    assert test_stack.group.head.val == 1


def test_pop_3(create_empty_stack):
    with pytest.raises(AttributeError):
        test_stack = create_empty_stack
        test_stack.pop()
