#!/usr/bin/env python

from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, itr=None):
        self.head = None
        self.length = 0
        if itr is not None:
            for item in itr:
                self.insert(item)

    def insert(self, val):
        """insert(val) will insert the value 'val' at the head of the list"""

        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """pop() will pop the first value off the head of
        the list and return it."""
        try:
            to_delete = self.head.val
            self.head = self.head.next
            self.length -= 1
            return to_delete
        except AttributeError:
            return 0

    def size(self):
        """size() will return the length of the list"""
        return self.length

    def search(self, val):
        """search(val) will return the node containing
        'val' in the list, if present, else None"""

        cur = self.head
        while cur is not None:
            if cur.val == val:
                break
            cur = cur.next
        return cur

    def remove(self, node):
        """remove(node) will remove the given node from
        the list, wherever it might be (node must be an item in the list)"""

        # Special case - remove first node
        if self.head is node:
            self.head = self.head.next
        # Else, iterate through list
        else:
            cur = self.head
            while cur is not None:
                if cur.next is node:
                    cur.next = cur.next.next
                    self.size -= 1
                    return
                cur = cur.next
            # if you get here, then node is not in the list, so throw an error
            raise LookupError('Node is not in the list.')

    def display(self):
        cur = self.head
        out = ""
        while cur:
            out += "{}, ".format(cur.val)
            cur = cur.next
        out = "({})".format(out.rstrip(', '))
        return out

    def __repr__(self):
        return str(self.display())

    def __str__(self):
        return self.display()
