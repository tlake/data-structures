# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, priority, order, value):
        self.priority = priority
        self.value = value
        self.order = order


class PriorityQueue(object):
    def __init__(self, itr=None):
        self.insertion_order = 0
        self.heap = []
        if itr is not None:
            for tup in itr:
                p, v = tup
                self.insert(p, v)

    def insert(self, priority, value):
        """Creates a Node with the given priority and value, and
        inserts it into the PriorityQueue."""
        self.insertion_order += 1
        node = Node(priority, self.insertion_order, value)
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        """Removes the highest-priority and first-inserted item
        from the PriorityQueue."""
        tmp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return tmp

    # .peek(): returns the most important item without removing it from
    # the queue.
    def peek(self):
        return self.heap[0].value

    def swap(self, p_index, c_index):
        """Swaps the node at p_index with the node at c_index."""
        temp = self.heap[p_index]
        self.heap[p_index] = self.heap[c_index]
        self.heap[c_index] = temp

    def heapify_up(self, child_index):
        if child_index != 0:
            parent_index = (child_index - 1) >> 1
            if self.heap[parent_index].priority < self.heap[child_index].priority:
                self.swap(child_index, parent_index)
                self.heapify_up(parent_index)
            elif self.heap[parent_index].priority == self.heap[child_index].priority:
                if self.heap[parent_index].order > self.heap[child_index].order:
                    self.swap(child_index, parent_index)
                    self.heapify_up(parent_index)

    def heapify_down(self, p_index):
        lc_index = 2 * p_index + 1
        rc_index = 2 * p_index + 2
        largest_index = p_index

        if lc_index < len(self.heap):
            if self.heap[largest_index].priority < self.heap[lc_index].priority:
                largest_index = lc_index
            elif self.heap[largest_index].priority == self.heap[lc_index].priority:
                if self.heap[largest_index].order > self.heap[lc_index].order:
                    largest_index = lc_index
        if rc_index < len(self.heap):
            if self.heap[largest_index].priority < self.heap[rc_index].priority:
                largest_index = rc_index
            elif self.heap[largest_index].priority == self.heap[rc_index].priority:
                if self.heap[largest_index].order > self.heap[rc_index].order:
                    largest_index = rc_index
        if largest_index != p_index:
            self.swap(p_index, largest_index)
            self.heapify_down(largest_index)


"""
    if p_pri < c_pri:
        swap
    elif p_pri == c_pri:
        if p_ord > c_ord:
            swap
    Given:
        Node
            pri
            ord
            val
        incrementing insertion counter
        Rule1: p_pri > c_pri
        Rule2: Given Rule1: p_ord < c_ord

    if p_pri < c_pri:
        swap
    elif p_pri == c_pri:
        if p_ord > c_ord:
            swap
"""
