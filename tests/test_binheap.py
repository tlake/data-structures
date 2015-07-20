# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from data_structures.bin_heap import BinaryHeap
import pytest


@pytest.fixture()
def create_binheap():
    """Creates a binary heap with an arbitrary list of numbers to use
    for further testing.
    """
    heap = BinaryHeap([15, 13, 2, 85, 106, 42, 3, 25])
    return heap


@pytest.fixture()
def create_empty_binheap():
    """Creates an empty binary heap"""
    heap = BinaryHeap()
    return heap


def test_binheap_push(create_binheap):
    """Insures that push inserts the value in the appropriate place
    """
    binheap = create_binheap
    binheap.push(125)
    assert binheap.heap[0] == 125
    binheap.push(4)
    assert binheap.heap[0] == 125
    assert binheap.heap[binheap.size - 1] == 4


def test_binheap_length(create_binheap, create_empty_binheap):
    """Makes sure that all the values are being added to the
    binary heap.
    """
    binheap = create_empty_binheap
    assert create_empty_binheap.size == 0
    binheap = create_binheap
    assert binheap.size == 8


def test_binheap_push_when_empty(create_empty_binheap):
    """Ensures the heap can accept values when empty"""
    binheap = create_empty_binheap
    binheap.push(125)
    assert binheap.heap[0] == 125


def test_binheap_pop(create_binheap):
    """pop(val) will pop the value from the top and rearrange
    all other values
    """
    binheap = create_binheap
    assert binheap.heap[0] == 106
    binheap.pop()
    assert binheap.heap[0] == 85
    binheap.pop()
    assert binheap.heap[0] == 42
    binheap.pop()
    assert binheap.heap[0] == 25
    binheap.pop()
    assert binheap.heap[0] == 15
    binheap.pop()
    assert binheap.heap[0] == 13
    binheap.pop()
    assert binheap.heap[0] == 3
    binheap.pop()
    assert binheap.heap[0] == 2


def test_binheap_pop_when_empty(create_empty_binheap):
    """Ensures that an exception is raised when trying
    to remove anything from an empty heap.
    """
    with pytest.raises(IndexError):
        binheap = create_empty_binheap
        binheap.pop()
