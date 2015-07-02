# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, priority, order, value):
        self.priority = priority
        self.value = value
        self.order = order


class PriorityQueue(object):
    def __init__(self):
        self.insertion_order = 0
        self.heap = []

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
        return self.heap[0]

    def swap(self, p_index, c_index):
        """Swaps the node at p_index with the node at c_index."""
        temp = self.heap[p_index]
        self.heap[p_index] = self.heap[c_index]
        self.heap[c_index] = temp
        return p_index, c_index

    def compare(self, p_index, c_index):
        pass
    #   if heap[p_index].pri < heap[c_index].pri:
    #     swap
    # elif p_pri == c_pri:
    #     if p_ord > c_ord:
    #         swap

    def heapify_up(self, child):
        if child != 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                self.swap(child, parent)
                self.heapify_up(parent)

    def heapify_down(self, index):
        """A parent at index i locates its two children's indexes with:
        2i + 1 and 2i + 2
        A child at index i finds its parent's index with:
        (i - 1) // 2
        """
        parent_node = self.heap[index]
        left_child_index = 2 * index + 1
        left_child_node = self.heap[left_child_index]
        right_child_index = 2 * index + 2
        right_child_node = self.heap[right_child_index]
        index_of_largest = index
        largest_node = self.heap[index_of_largest]
        #  make sure left is not out of bounds
        #  then make sure left is not bigger than the biggest node
        if left_child_index < len(self.heap):
            if left_child_node.priority > right_child_node.priority:
                index_of_largest = left_child_index
            elif left_child_node.priority == right_child_node.priority:
                if left_child_node.order > parent_node.order:
                    index_of_largest = left_child_index
        #  make sure right is not bigger than the biggest node
        elif right_child_index < len(self.heap):
            if right_child_node.priority > largest_node.priority:
                index_of_largest = right_child_index
        #  make the swap
        if index_of_largest != index:
            self.swap(index, index_of_largest)
            #  do it again
            self.heapify_down(index_of_largest)


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
