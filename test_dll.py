# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from doubly_linked_list import DoublyLinkedList
import pytest


@pytest.fixture()
def create_dll():
    dll = DoublyLinkedList([1, 2, 3])
    return dll


# insert(val) will insert the value 'val' at the head of the list
def test_dll_insert(create_dll):
    dll = create_dll.insert('insertion')
    assert dll.head.val == 'insertion'


# append(val) will append the value 'val' at the tail of the list
def test_dll_append(create_dll):
    dll = create_dll.append('appenditure')
    assert dll.tail.val == 'appenditure'


# pop() will pop the first value off the head of the list and return it.
def test_dll_pop(create_dll):
    dll = create_dll
    head_val = dll.head.val
    popped_val = dll.pop()
    assert head_val == popped_val


# shift() will remove the last value from the tail of the list and return it.


# remove(val) will remove the first instance of 'val' found in the list,
# starting from the head. If 'val' is not present, it will raise an
# appropriate Python exception.
