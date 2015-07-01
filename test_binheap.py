# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bin_heap import BinaryHeap
import pytest


@pytest.fixture()
def create_binheap():
    return BinaryHeap([5, 13, 2, 85, 106, 42, 3, 25])


@pytest.fixture()
def create_empty_binheap():
    return BinaryHeap([])


# push(val) will insert the value 'val' in the appropriate place
def test_binheap_push(create_binheap):
    binheap = create_binheap
    binheap.push(125)
    assert binheap.top == 125
    binheap.push(4)
    assert binheap.top == 125


def test_binheap_push_when_empty(create_empty_binheap):
    binheap = create_empty_binheap
    binheap.push(125)
    assert binheap.top == 125


# pop(val) will pop the value 'val' from the top
def test_binheap_pop(create_binheap):
    binheap = create_binheap
    binheap.pop()
    assert binheap.top == 85


def test_binheap_pop_when_empty(create_empty_binheap):
    with pytest.raises(Exception):
        binheap = create_empty_binheap
        binheap.pop("this heap is empty")
