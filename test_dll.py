# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from doubly_linked_list import DoublyLinkedList
import pytest


@pytest.fixture()
def create_dll():
    return DoublyLinkedList([1, 2, 3])


@pytest.fixture()
def create_empty_dll():
    return DoublyLinkedList()


# insert(val) will insert the value 'val' at the head of the list
def test_dll_insert(create_dll):
    dll = create_dll
    dll.insert('insertion')
    assert dll.head.val == 'insertion'


def test_dll_insert_when_empty(create_empty_dll):
    dll = create_empty_dll
    dll.insert('insertion')
    assert dll.head.val == 'insertion'
    assert dll.tail.val == 'insertion'


# append(val) will append the value 'val' at the tail of the list
def test_dll_append(create_dll):
    dll = create_dll
    dll.append('appenditure')
    assert dll.tail.val == 'appenditure'


# pop() will pop the first value off the head of the list and return it.
def test_dll_pop(create_dll):
    dll = create_dll
    head_val = dll.head.val
    popped_val = dll.pop()
    assert head_val == popped_val


# shift() will remove the last value from the tail of the list and return it.
def test_dll_shift(create_dll):
    dll = create_dll
    tail_val = dll.tail.val
    shifted_val = dll.shift()
    assert tail_val == shifted_val


# remove(val) will remove the first instance of 'val' found in the list,
# starting from the head. If 'val' is not present, it will raise an
# appropriate Python exception.
