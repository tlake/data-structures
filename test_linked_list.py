#!/usr/bin/env python

import pytest
import sys
import subprocess

from linked_list import LinkedList


def test_LinkedList():
    assert LinkedList([1, 2, 3]).head.val == 3


def test_insert():
    l1 = LinkedList([1, 2, 3])
    l1.insert(4)
    assert l1.head.val == 4


def test_pop():
    pop1 = LinkedList([1, 2, 3])
    pop1.pop()
    assert pop1.head.val == 2


def test_size():
    size1 = LinkedList([1, 2, 3])
    assert size1.size() == 3
    size1.pop()
    assert size1.size() == 2


def test_search():
    search1 = LinkedList([1, 2, 3])
    assert search1.search(3).val == 3


def test_remove():
    remove1 = LinkedList([1, 2, 3])
    remove1.remove(remove1.search(3))
    assert remove1.head.val == 2


def test_display():
    display1 = LinkedList([1, 2, 3]).display()
    assert display1 == '(3, 2, 1)'
