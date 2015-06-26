# -*- coding: utf-8 -*-
from linked_list import LinkedList


class Stack(object):
    def __init__(self, itr=None):
        self.group = LinkedList(itr)

    def pop(self):
        return self.group.pop()

    def push(self, val):
        self.group.insert(val)
