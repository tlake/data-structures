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
        """adds to the end of the list and bubbles up to the right
        position.
        """
        self.heap.append(val)
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self, child):
        if child != 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                self.swap(child, parent)
                self.heapify_up(parent)

    def pop(self):
        """removes the top of the heap and resorts the resorts the rest.
        """
        tmp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return tmp

    def heapify_down(self, index):
        """A parent at index i locates its two children's indexes with:
        2i + 1 and 2i + 2
        A child at index i finds its parent's index with:
        (i - 1) // 2
        """
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest_child = index
        #  make sure left is not out of bounds, then
        #  make sure left is not bigger than the biggest node
        if (left_child < self.size and
           self.heap[left_child] > self.heap[largest_child]):
            largest_child = left_child
        #  make sure right is not bigger than the biggest node
        if (right_child < self.size and
           self.heap[right_child] > self.heap[largest_child]):
            largest_child = right_child
        #  make the swap
        if largest_child != index:
            self.swap(index, largest_child)
            #  do it again
            self.heapify_down(largest_child)

    def swap(self, small, large):
        """Swaps the smaller value with the larger value.
        """
        temp = self.heap[large]
        self.heap[large] = self.heap[small]
        self.heap[small] = temp
        return large, small
