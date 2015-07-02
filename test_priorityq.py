# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from priorityq import PriorityQueue
import pytest


@pytest.fixture()
def create_pq():
    """Creates a priotity queue with an arbitrary list of numbers to use
    for further testing.
    """
    pq = PriorityQueue([15, 13, 2, 85, 106, 42, 3, 25])
    return pq


@pytest.fixture()
def create_pq2():
    """Creates a priotity queue with an arbitrary list of numbers to use
    for further testing.
    """
    pq = PriorityQueue()
    pq.insert((1, "We"))
    pq.insert((2, "eee"))
    pq.insert((1, "eee"))
    pq.insert((3, "are"))
    pq.insert((1, "the"))
    pq.insert((4, "champions"))
    pq.insert((1, "my"))
    pq.insert((5, "friends"))
    return pq


@pytest.fixture()
def create_empty_pq():
    """Creates an empty priotity queue"""
    pq = PriorityQueue()
    return pq

#
#  Test Insert
#
def test_pq_insert1(create_pq):
    """Insures that insert inserts the value in the appropriate place
    """
    pq = create_pq
    #  If you add an item with the highest priority,
    #  It will always be at the top of the list.
    pq.insert((101, "Test1"))
    assert pq.heap[0].value == "Test1"
    pq.insert((102, "Test2"))
    assert pq.heap[0].value == "Test2"
    pq.insert((103, "Test3"))
    assert pq.heap[0].value == "Test3"

    #  If you add an item with the lowest priority,
    #  It will always be at the bottom of the list.
    pq.insert((104, "Test4"))
    assert pq.heap[0].value == "Test4"
    pq.insert((105, "Test5"))
    assert pq.heap[0].value == "Test5"
    pq.insert((106, "Test6"))
    assert pq.heap[0].value == "Test6"


def test_pq_insert2(create_pq):
    """pop(val) will pop the value from the top and rearrange
    all other values
    """
    pq = PriorityQueue()
    pq.insert((1, "We"))
    assert pq.heap[0] == "We"
    pq.insert((2, "eee"))
    assert pq.heap[0] == "eee"
    pq.insert((1, "eee"))
    assert pq.heap[0] == "eee"
    pq.insert((3, "are"))
    assert pq.heap[0] == "are"
    pq.insert((1, "the"))
    assert pq.heap[0] == "are"
    pq.insert((4, "champions"))
    assert pq.heap[0] == "champions"
    pq.insert((1, "my"))
    assert pq.heap[0] == "champions"
    pq.insert((5, "friends"))
    assert pq.heap[0] == "friends"


def test_pq_length(create_pq, create_empty_pq):
    """Makes sure that all the values are being added to the
    priotity queue.
    """
    pq = create_empty_pq
    assert len(pq.heap) == 0
    pq = create_pq
    assert len(pq.heap) == 8


def test_pq_pop(create_pq):
    """pop(val) will pop the value from the top and rearrange
    all other values to maintain the priority queue/max heap property
    """
    pq = create_pq
    assert pq.heap[0] == "friends"
    pq.pop()
    assert pq.heap[0] == "champions"
    pq.pop()
    assert pq.heap[0] == "are"
    pq.pop()
    assert pq.heap[0] == "eee"
    pq.pop()
    assert pq.heap[0] == "We"
    pq.pop()
    assert pq.heap[0] == "eee"
    pq.pop()
    assert pq.heap[0] == "the"
    pq.pop()
    assert pq.heap[0] == "my"


def test_pq_pop_when_empty(create_empty_pq):
    """Ensures that an exception is raised when trying
    to pop() from an empty heap.
    """
    with pytest.raises(IndexError):
        pq = create_empty_pq
        pq.pop()
