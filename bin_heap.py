#!/usr/bin/env python

from __future__ import unicode_literals


class BinaryHeap(object):
    def __init__(self, itr=None):
        self.heap = []
        self.size = 0
        if itr is not None:
            for val in itr:
                self.push(val)

    def push(self, val):
        self.heap.append(val)
        self.size += 1
        self.max_heapify2(self.size-1)

    def max_heapify2(self, child):
        if child != 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                self.swap(child, parent)
                self.max_heapify2(parent)

    def pop(self):
        tmp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.max_heapify(0)
        return tmp

    def max_heapify(self, index):
        # A parent at index i locates its two children's indexes with:
        # 2i + 1 and 2i + 2
        # A child at index i finds its parent's index with:
        #  (i - 1) // 2
        #import pdb; pdb.set_trace()
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        #  make sure left is not out of bounds, then
        #  make sure left is not bigger than the biggest node
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        #  make sure right is not bigger than the biggest node
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        #  make the swap
        if largest != index:
            self.swap(index, largest)
            #  do it again
            self.max_heapify(largest)

    def swap(self, small, large):
        temp = self.heap[large]
        self.heap[large] = self.heap[small]
        self.heap[small] = temp
        return large, small
