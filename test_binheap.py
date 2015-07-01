# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bin_heap import BinaryHeap
import pytest


@pytest.fixture()
def create_binheap():
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
    heap = BinaryHeap()
    return heap


# push(val) will insert the value 'val' in the appropriate place
def test_binheap_push(create_binheap):
    binheap = create_binheap
    binheap.push(125)
    assert binheap.heap[0] == 125
    binheap.push(4)
    assert binheap.heap[0] == 125
    assert binheap.heap[8] == 4


def test_binheap_length(create_binheap):
    binheap = create_binheap
    assert len(binheap.heap) == 8


def test_binheap_push_when_empty(create_empty_binheap):
    binheap = create_empty_binheap
    binheap.push(125)
    assert binheap.heap[0] == 125


# pop(val) will pop the value 'val' from the top
def test_binheap_pop(create_binheap):
    binheap = create_binheap
    binheap.pop()
    assert binheap.heap[0] == 85
    binheap.pop()
    assert binheap.heap[0] == 42


def test_binheap_pop_when_empty(create_empty_binheap):
    with pytest.raises(Exception):
        binheap = create_empty_binheap
        binheap.pop("this heap is empty")


def test_max_heapify_empty_heap(create_empty_binheap):
    with pytest.raises(Exception):
        binheap = create_empty_binheap
        binheap.max_heapify("this heap is empty")
