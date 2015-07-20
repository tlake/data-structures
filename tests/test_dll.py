# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from data_structures.doubly_linked_list import DoublyLinkedList
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
def test_dll_remove(create_dll):
    dll = create_dll

    # create the values we'll be using
    testing_val = 4
    new_head_val = 5

    # insert and append testing_val so that head.val and tail.val
    # are the same
    dll.insert(testing_val)
    dll.append(testing_val)

    # insert new_head_val so that testing_val is not the head, but instead
    # now occurs at the second node of the list (as well as the tail)
    dll.insert(new_head_val)

    # assert that we've done those things correctly
    assert dll.head.next.val == testing_val
    assert dll.tail.val == testing_val

    # call .remove() with testing_val, which ought to remove the second
    # node, but leave the tail node as is
    dll.remove(testing_val)

    # assert that the head node is unchanged, that the second node's value
    # is no longer the same as testing_value, and that the tail node's value
    # *IS* still the same as testing_value
    assert dll.head.val == new_head_val
    assert dll.tail.val == testing_val
    assert dll.head.next.val != testing_val


def test_dll_remove_not_found(create_dll):
    with pytest.raises(LookupError):
        dll = create_dll
        dll.remove("this doesn't exist in the list")
