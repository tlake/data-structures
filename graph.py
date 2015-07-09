#!/usr/bin/env python

from __future__ import unicode_literals


class Graph(object):
    def __init__(self):
        self.graph = {}

    def nodes(self):
        """Returns a list of all nodes in the graph."""
        return self.graph.keys()

    def edges(self):
        """Returns a list of all edges in the graph."""
        edges = []
        for node, neighbors in self.graph.iteritems():
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges

    def add_node(self, new_node, neighbors=[]):
        """Adds a new node to the graph"""
        if new_node not in self.nodes():
            self.graph[new_node] = []
            for node in neighbors:
                self.add_edge(new_node, node)
        else:
            raise ValueError("Node is already in the list.")

    def add_edge(self, node1, node2):
        """Adds a new edge to the graph connecting node1 to node2.
        If either node1 or node2 are not already present in the
        graph, they are added."""
        self.graph.setdefault(node1, []).append(node2)
        self.graph.setdefault(node2, [])

    def del_node(self, del_node):
        """Deletes the node from the graph. Raises an error if no
        such node exists"""
        if del_node in self.graph.keys():
            del(self.graph[del_node])
            for node in self.graph.keys():
                if del_node in self.graph[node]:
                    self.graph[node].remove(del_node)
        else:
            raise IndexError("Node not in graph")

    def del_edge(self, node1, node2):
        """Deletes the edge connecting node1 and node2 from the graph.
        Raises an error if no such edge exists."""
        if (node1, node2) in self.edges():
            self.graph[node1].remove(node2)
        else:
            raise IndexError("Edge not in graph")

    def has_node(self, node):
        """True if node is in the graph, False if it is not."""
        if node in self.graph.keys():
            return True
        else:
            return False

    def neighbors(self, node):
        """Returns a list of all nodes connected to node by edges.
        Raises an error if node is not in the graph."""
        return self.graph[node]

    def adjacent(self, node1, node2):
        """Returns True if there is an edge connecting node1 and node2.
        False if no such edge exists. Raises an error if either of the
        supplied nodes are not in the graph."""
        if (node1 not in self.graph.iterkeys()
           or node2 not in self.graph.iterkeys()):
            raise KeyError
        verdict = False
        if node2 in self.graph[node1]:
            verdict = True
        return verdict

    def depth_first_traversal(self, node):
        result = []

        def traverse(node):
            if node not in result:
                result.append(node)
                for neighbor in self.neighbors(node):
                    traverse(neighbor)
        traverse(node)
        return result
