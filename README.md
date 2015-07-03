# data-structures

Authors:

- [Megan Slater](https://github.com/meslater1030)
- [Tanner Lake](https://github.com/tlake)
- [Tyler Peek](https://github.com/tpeek)

## Summary:
A repository to hold sample code for a number of classic data structures implemented in Python.


### Singly Linked List:
Contains a Node class that holds a variable and a pointer to the next Node.

**Methods:** \_\_init\__, \_\_repr\_\_, \_\_str\_\_, insert, pop, size, search, remove, dequeue, display


### Doubly-Linked List:
Contains a Node class that holds a variable and two pointers: one to the previous Node and one to the Next Node.

**Methods:** insert, append, pop, shift, remove


### Stack:
A Last In, First Out(LIFO) structure.  Contains a LinkedList that keeps track of the objects passed in.

**Methods:** push, pop


### Parethetics:
A function that takes in a string and:
    Return 1 if the string is "open" (there are open parens that are not closed)
    Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
    Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)
It also takes an optional argument of a string of two characters. The first will act as an opening symbol and the second as a closing symbol.


### Queue:
A First In, First Out(FIFO) structure.  Contains a LinkedList that keeps track of the objects passed in as well as the size.

**Methods:** enqueue, dequeue, size


### Binary Heap:
Contains a BinaryHeap class with the following methods:

- .push()
  * puts a new value into the heap, maintaining the heap property.
- .pop():
  * removes the "top" value in the heap, maintaining the heap property.
- .heapify_up()
  * compares a child to its parent and swaps them if the child is larger
- .heapify_down()
  * compares a parent to its left child and swaps them if the parent is smaller;
else compares the parent to its right child and swaps them if the parent is smaller

The heap constructor defaults to creating an empty heap, but allows for creating a populated heap if given an iterable as an input.

Visual assistance provided by [BinaryTreeVisualiser](http://btv.melezinek.cz/binary-heap.html)


### Priority Queue:
Contains a Node that holds variable, order and priority values.  Also contains a Priority Queue class that organizes Nodes in a binary heap so that node returned is the node with that highest priority that was added first.

**Methods:**  insert, pop, peek

[![Travis](https://travis-ci.org/tlake/data-structures.svg)](https://travis-ci.org/tlake/data-structures.svg)