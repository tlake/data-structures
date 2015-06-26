#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from linked_list import LinkedList, Node


@pytest.fixture()
def create_linked_list():
    return LinkedList([1, 2, 3])


@pytest.fixture()
def create_empty_list():
    return LinkedList()


@pytest.fixture()
def create_unpointed_node():
    return Node(1)


def test_linked_list(create_linked_list):
    assert create_linked_list.head.val == 3


def test_insert(create_linked_list):
    l1 = create_linked_list
    l1.insert(4)
    assert l1.head.val == 4


def test_pop(create_linked_list):
    pop1 = create_linked_list
    pop1.pop()
    assert pop1.head.val == 2


def test_size(create_linked_list):
    size1 = create_linked_list
    assert size1.size() == 3
    size1.pop()
    assert size1.size() == 2


def test_search(create_linked_list):
    search1 = create_linked_list
    assert search1.search(3).val == 3


def test_remove_head(create_linked_list):
    l_list = create_linked_list
    second_head = l_list.head.next
    l_list.remove(l_list.head)
    assert l_list.head == second_head


def test_remove_on_empty_error(create_empty_list, create_unpointed_node):
    with pytest.raises(LookupError):
        empty_list = create_empty_list
        empty_list.remove(create_unpointed_node)


def test_display(create_linked_list):
    display1 = create_linked_list.display()
    assert display1 == '(3, 2, 1)'
