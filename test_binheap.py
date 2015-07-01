# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bin_heap import BinaryHeap
import pytest


@pytest.fixture()
def create_binheap():
    """Creates a binary heap with an arbitrary list of numbers to use
    for further testing.
    """
    heap = BinaryHeap()
    heap.push(5)
    heap.push(13)
    heap.push(2)
    heap.push(85)
    heap.push(106)
    heap.push(42)
    heap.push(3)
    heap.push(25)
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
    assert binheap.heap[9] == 4


def test_binheap_length(create_binheap):
    """Makes sure that all the values are being added to the
    binary heap.
    """
    binheap = create_binheap
    assert len(binheap.heap) == 8


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
    binheap.pop()
    assert binheap.heap[0] == 85
    binheap.pop()
    assert binheap.heap[0] == 42


def test_binheap_pop_when_empty(create_empty_binheap):
    """Ensures that an exception is raised when trying
    to remove anything from an empty heap.
    """
    with pytest.raises(Exception):
        binheap = create_empty_binheap
        binheap.pop("this heap is empty")
