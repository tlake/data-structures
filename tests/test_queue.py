#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from data_structures.queue import Queue


@pytest.fixture()
def create_queue():
    return Queue([1, 2, 3])


@pytest.fixture()
def create_empty_queue():
    return Queue()


@pytest.fixture
def create_single_item_queue():
    return Queue([1])


def test_dequeue(create_queue):
    assert create_queue.dequeue() == 1


def test_dequeue_2(create_single_item_queue):
    assert create_single_item_queue.dequeue() == 1


def test_enqueue(create_queue):
    test_queue = create_queue
    test_queue.enqueue(4)
    assert test_queue.list.head.val == 4


def test_enqueue_to_empty_queue(create_empty_queue):
    test_queue = create_empty_queue
    test_queue.enqueue(1)
    assert test_queue.list.head.val == 1


def test_dequeue_3(create_empty_queue):
    with pytest.raises(IndexError):
        test_queue = create_empty_queue
        test_queue.dequeue()


def test_size(create_empty_queue, create_queue, create_single_item_queue):
    test_empty_queue = create_empty_queue
    test_create_queue = create_queue
    test_create_single_item_queue = create_single_item_queue
    assert test_empty_queue.size() == 0
    assert test_create_queue.size() == 3
    assert test_create_single_item_queue.size() == 1


def test_add_and_remove(create_empty_queue):
    test_queue = create_empty_queue
    test_queue.enqueue(4)
    test_queue.dequeue()
    assert test_queue.size() == 0
