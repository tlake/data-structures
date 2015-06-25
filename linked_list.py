#!/usr/bin/env python


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self, itr):
        self.head = None
        self.length = 0
        for item in itr:
            self.insert(item)

    def insert(self, val):
        """insert(val) will insert the value 'val' at the head of the list"""
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.length += 1

    def pop(self):
        """pop() will pop the first value off the head of
        the list and return it."""
        to_delete = self.head
        self.head = self.head.next
        self.length -= 1
        return to_delete

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
        the list, wherever it might be (node must be an item in the list"""
        if self.head == node:
            return self.pop()
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.val == node.val:
                prev.next = prev.next.next
            cur = cur.next
            prev = prev.next

    def display(self):
        """display() will print the list represented as a Python
        tuple literal: "(12, 'sam', 37, 'tango')" """
        # cur = self.head
        # tup = (cur.val,)
        # cur = cur.next
        # while cur is not None:
        #     tup = tup + (cur.val,)
        #     cur = cur.next
        # return tup

        cur = self.head
        tup = repr(cur.val)
        cur = cur.next
        while cur is not None:
            tup = tup + ", " + repr(cur.val)
            cur = cur.next
        return "(" + tup + ")"

    def __repr__(self):
        return str(self.display())

    def __str__(self):
        return self.display()
