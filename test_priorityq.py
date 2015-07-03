# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from priorityq import PriorityQueue
import pytest


@pytest.fixture()
def create_pq():
    """Creates a priotity queue, then inserts priorities and values to use
    for further testing.
    """
    pq = PriorityQueue()
    pq.insert(1, "We")
    pq.insert(2, "eee")
    pq.insert(1, "eee")
    pq.insert(3, "are")
    pq.insert(1, "the")
    pq.insert(4, "champions")
    pq.insert(1, "my")
    pq.insert(5, "friends")
    return pq


def test_pq_insert1(create_pq):
    """Insures that insert inserts the value in the appropriate place
    """
    pq = create_pq
    #  If you add an item with the highest priority,
    #  It will always be at the top of the list.
    pq.insert(101, "Test1")
    assert pq.heap[0].value == "Test1"
    pq.insert(102, "Test2")
    assert pq.heap[0].value == "Test2"
    pq.insert(103, "Test3")
    assert pq.heap[0].value == "Test3"

    #  If you add an item with the lowest priority,
    #  It will always be at the bottom of the list.
    #  AKA heapify up will never do anything.
    pq.insert(-1, "Test4")
    assert pq.heap[len(pq.heap)-1].value == "Test4"
    pq.insert(-2, "Test5")
    assert pq.heap[len(pq.heap)-1].value == "Test5"
    pq.insert(-3, "Test6")
    assert pq.heap[len(pq.heap)-1].value == "Test6"


def test_pq_insert2():
    """Test that inserting into a priority queue
    behaves as expected.
    """
    pq = PriorityQueue()
    pq.insert(1, "We")
    assert pq.heap[0].value == "We"
    pq.insert(2, "eee")
    assert pq.heap[0].value == "eee"
    pq.insert(1, "eee")
    assert pq.heap[0].value == "eee"
    pq.insert(3, "are")
    assert pq.heap[0].value == "are"
    pq.insert(1, "the")
    assert pq.heap[0].value == "are"
    pq.insert(4, "champions")
    assert pq.heap[0].value == "champions"
    pq.insert(1, "my")
    assert pq.heap[0].value == "champions"
    pq.insert(5, "friends")
    assert pq.heap[0].value == "friends"


def test_pq_length(create_pq):
    """Makes sure that the size is correct after adding
    to the priotity queue.
    """
    pq = PriorityQueue()
    assert len(pq.heap) == 0
    pq = create_pq
    assert len(pq.heap) == 8


def test_pq_pop(create_pq):
    """pop(val) will pop the value from the top and rearrange
    all other values to maintain the priority queue/max heap property
    """
    pq = create_pq
    assert pq.pop() == "friends"
    assert pq.pop() == "champions"
    assert pq.pop() == "are"
    assert pq.pop() == "eee"
    assert pq.pop() == "We"
    assert pq.pop() == "eee"
    assert pq.pop() == "the"
    assert pq.pop() == "my"


def test_pop_single(create_pq):
    pq = PriorityQueue()
    pq.insert(1, "Almost missed this")
    assert pq.pop() == "Almost missed this"


def test_pq_pop_when_empty():
    """Ensures that an exception is raised when trying
    to pop() from an empty priority heap.
    """
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek(create_pq):
    """Ensures that peek raises an error when the priority queue
    is empty, and that it returns the right value when items are added.
    """
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()
    pq = create_pq
    pq.insert(100, "This is so much fun!")
    assert pq.peek() == "This is so much fun!"
    assert pq.peek() != "This sucks"
