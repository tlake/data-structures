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
        #  do fun stuff

    def pop(self):
        tmp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)
        return tmp

    def max_heapify(self, index):
        # A parent at index i locates its two children's indexes with:
        # 2i + 1 and 2i + 2
        # A child at index i finds its parent's index with:
        #  (i - 1) // 2
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        #  make sure left is not out of bounds, then
        #  make sure left is not bigger than the biggest node
        if left < self.size and self.heap[left] > self.heap[index]:
            largest = right
        #  make sure right is not bigger than the biggest node
        if right < self.size and self.heap[right] > self.heap[index]:
            largest = left
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
