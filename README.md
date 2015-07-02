# data-structures
Authors: Megan Slater, Tanner Lake, Tyler Peek

### Summary:
A repository to hold sample code for a number of classic data structures implemented in Python.


### Singly Linked List:
Contains a Node class that holds a variable and a pointer to the next Node.
**Methods:** __init__, __repr__, __str__, insert, pop, size, search, remove, dequeue, display

### Doubly-Linked List:
Contains a Node class that holds a variable and two pointers: one to the previous Node and one to the Next Node.
**Methods:** insert, append, pop, shift, remove

### Stack:
A Last In, First Out(LIFO) structure.  Contains a LinkedList that keeps track of the objects passed in.
Methods: push, pop

### Parethetics:
A function that takes in a string and:
    Return 1 if the string is "open" (there are open parens that are not closed)
    Return 0 if the string is "balanced" (there are an equal number of open and closed parentheses in the string)
    Return -1 if the string is "broken" (a closing parens has not been proceeded by one that opens)
It also takes an optional argument of a string of two characters. The first will act as an opening symbol and the second as a closing symbol.

### Queue:
A First In, First Out(FIFO) structure.  Contains a LinkedList that keeps track of the objects passed in as well as the size.
**Methods:**  enqueue, dequeue, size


### Binary Heap:
Contains a Binary Heap object that accepts an interable and sorts the values into a binary heap.
**Methods:**  push, pop

Visual assistance provided by [BinaryTreeVisualiser](http://btv.melezinek.cz/binary-heap.html)

### Priority Queue:
Contains a Node that holds variable, order and priority values.  Also contains a Priority Queue class that organizes Nodes in a binary heap so that node returned is the node with that highest priority that was added first.
**Methods:**  insert, pop, peek

[![Travis](https://travis-ci.org/tlake/data-structures.svg)](https://travis-ci.org/tlake/data-structures.svg)