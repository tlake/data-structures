#!/usr/bin/env python

from __future__ import unicode_literals


class Graph(object):
    def __init__(self):
        self.graph = {}

    def nodes(self):
        """Returns a list of all nodes in the graph."""
        keys = []
        for key in self.graph.iterkeys():
            keys.append(key)
        return keys

    def edges(self):
        """Returns a list of all edges in the graph."""
        nodes = self.nodes()
        edges = []
        for node in nodes:
            edges.append(self.graph[node])
        return edges

    def add_node(self, new_node):
        """Adds a new node to the graph"""
        self.graph[new_node] = []

    def add_edge(self, node1, node2):
        """Adds a new edge to the graph connecting node1 to node2.
        If either node1 or node2 are not already present in the
        graph, they are added."""
        pass

    def del_node(self, node):
        """Deletes the node from the graph. Raises an error if no
        such node exists"""
        pass

    def del_edge(self, node1, node2):
        """Deletes the edge connecting node1 and node2 from the graph.
        Raises an error if no such edge exists."""
        pass

    def has_node(self, node):
        """True if node is in the graph, False if it is not."""
        pass

    def neighbors(self, node):
        """Returns a list of all nodes connected to node by edges.
        Raises an error if node is not in the graph."""
        pass

    def adjacent(node1, node2):
        """Returns True if there is an edge connecting node1 and node2.
        False if no such edge exists. Raises an error if either of the
        supplied nodes are not in the graph."""
        pass

