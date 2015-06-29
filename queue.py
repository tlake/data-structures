#!/usr/bin/env python
from __future__ import unicode_literals
from linked_list import LinkedList

"""
enqueue(value): adds value to the queue
dequeue(): removes the correct item from the queue and returns
its value (should raise an error if the queue is empty) size():
return the size of the queue.  Should return 0 if the queue is
empty.
"""


class Queue(object):
    def __init__(self, itr=None):
        self.list = LinkedList(itr)

    def enqueue(self, val):
        self.list.insert(val)

    def dequeue(self):
        return self.list.dequeue()

    def size(self):
        return self.list.size()
