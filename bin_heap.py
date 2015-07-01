#!/usr/bin/env python

from __future__ import unicode_literals


class BinaryHeap(object):
    def __init__(self, itr=None):
        self.heap = []
        self.size = 0
        if itr is not None:
            for val in itr:
                pass

    def insert(self, val):
        self.heap.append(val)
        self.size += 1

    def max_heapify(self, index):
        #  a nodes child nodes are going to be at index
        #  2i and 2i+1, but only if you start at index 1.
        #  So you have to add 1 to the index passed in, do
        #  the math, then subtact 1 to get back at the actual
        #  indexes.
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)
        largest = index
        #  make sure left is not out of bounds, then
        #  make sure left is not bigger than the biggest node
        if left <= self.size and self.heap[left] > self.heap[0]:
            largest = right
        #  make sure right is not bigger than the biggest node
        if right <= self.size and self.heap[right] > self.heap[0]:
            largest = left
        #  make the swap
        if largest != index:
            self.swap(index, largest)
            #  do it again
            self.max_heapify(largest)

    def swap(self, small, large):
        temp = self.heap[small]
        self.heap[large] = self.heap[small]
        self.heap[small] = temp
        return large, small
