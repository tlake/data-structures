# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, priority, order, value):
        self.priority = priority
        self.value = value
        self.order = order


class PriorityQueue(object):
    """Creates a Priority Queue. If a list of tuples is sent in,
    they are each unpacked and sent to the insert method."""
    def __init__(self, itr=None):
        self.insertion_order = 0
        self.heap = []
        if itr is not None:
            for tup in itr:
                p, v = tup
                self.insert(p, v)

    def insert(self, priority, value):
        """Creates a Node with the given priority and value, and
        inserts it into the Priority Queue."""
        self.insertion_order += 1
        node = Node(priority, self.insertion_order, value)
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        """Removes the Node with the highest-priority and returns its value.
        If there is more than one Node with the same priority, the one that
        was inserted first will always be the one returned."""
        tmp = self.heap[0].value
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
        else:
            self.heap = []
            self.order = 0
        return tmp

    def peek(self):
        """Returns the most important item without removing it from
        the queue."""
        return self.heap[0].value

    def swap(self, p_index, c_index):
        """Swaps the parent node with the child node."""
        temp = self.heap[p_index]
        self.heap[p_index] = self.heap[c_index]
        self.heap[c_index] = temp

    def heapify_up(self, child_index):
        """Moves a newly inserted node up the heap by comparing it to
        its parent and swapping it if its priority is greater or if its
        priority is the same but its order is less."""
        if child_index != 0:
            parent_index = (child_index - 1) >> 1
            if (self.heap[parent_index].priority <
               self.heap[child_index].priority):
                self.swap(child_index, parent_index)
                self.heapify_up(parent_index)
            elif (self.heap[parent_index].priority ==
                  self.heap[child_index].priority):
                if (self.heap[parent_index].order >
                   self.heap[child_index].order):
                    self.heapify_up(parent_index)

    def heapify_down(self, p_index):
        """Moves the Node that replaced the top down down the heap by
        comparing it to its parent and swapping it if its priority is less
        or if its priority is the same but its order is greater."""
        lc_index = 2 * p_index + 1
        rc_index = 2 * p_index + 2
        largest_index = p_index

        if lc_index < len(self.heap):
            if (self.heap[largest_index].priority <
               self.heap[lc_index].priority):
                largest_index = lc_index
            elif (self.heap[largest_index].priority ==
                  self.heap[lc_index].priority):
                if self.heap[largest_index].order > self.heap[lc_index].order:
                    largest_index = lc_index
        if rc_index < len(self.heap):
            if (self.heap[largest_index].priority <
               self.heap[rc_index].priority):
                largest_index = rc_index
            elif (self.heap[largest_index].priority ==
                  self.heap[rc_index].priority):
                if self.heap[largest_index].order > self.heap[rc_index].order:
                    largest_index = rc_index
        if largest_index != p_index:
            self.swap(p_index, largest_index)
            self.heapify_down(largest_index)
