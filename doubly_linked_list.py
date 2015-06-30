#!/usr/bin/env python

from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self, itr=None):
        self.head = None
        self.tail = None
        self.length = 0
        if itr is not None:
            for item in itr:
                self.insert(item)

    def insert(self, val):
        """insert(val) will insert the value 'val'
        at the head of the list"""
        new_node = Node(val)
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, val):
        """append(val) will append the value 'val'
        at the tail of the list"""
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def pop(self):
        """pop() will pop the first value off the head of
        the list and return it."""

        to_delete = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return to_delete

    def shift(self):
        to_delete = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return to_delete

#     def size(self):
#         """size() will return the length of the list"""
#         return self.length

#     def search(self, val):
#         """search(val) will return the node containing
#         'val' in the list, if present, else None"""

#         cur = self.head
#         while cur is not None:
#             if cur.val == val:
#                 break
#             cur = cur.next
#         return cur

#     def remove(self, node):
#         """remove(node) will remove the given node from
#         the list, wherever it might be (node must be an item in the list)"""

#         # Special case - remove first node
#         if self.head is node:
#             self.head = self.head.next
#         # Else, iterate through list
#         else:
#             cur = self.head
#             while cur is not None:
#                 if cur.next is node:
#                     cur.next = cur.next.next
#                     self.size -= 1
#                 cur = cur.next
#             # if you get here, then node is not in the
# list, so throw an error
#             raise LookupError('Node is not in the list.')

#     def display(self):
#         cur = self.head
#         out = ""
#         while cur:
#             out += "{}, ".format(cur.val)
#             cur = cur.next
#         out = "({})".format(out.rstrip(', '))
#         return out

# #     def __repr__(self):
# #         return str(self.display())

#     def __str__(self):
#         return "{}, {}, {}".format(self.head.val, self.head.next.val, self.tail.val)
