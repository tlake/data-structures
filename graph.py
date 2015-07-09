#!/usr/bin/env python

from __future__ import unicode_literals
import queue


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

    def breadth_first_traversal(self, start):
        """Perform a full breadth-first traversal of the graph,
        beginning at start. Return the full visited path when
        traversal is complete."""

        # import pdb; pdb.set_trace()

        q = queue.Queue()
        q.enqueue(start)
        discovered = [start, ]

        def traverse(start):
            while q.size() > 0:
                node = q.dequeue()

                for neighbor in self.neighbors(node):
                    if neighbor not in discovered:
                        q.enqueue(neighbor)
                        discovered.append(neighbor)

                traverse(node)

        traverse(start)

        return discovered


if __name__ == "__main__":
    graph = Graph()
    nodes = [1, 2, 3, 4, 5]
    for n in nodes:
        graph.add_node(n)
    edges = [(1, 3), (1, 4), (2, 4), (2, 5), (3, 2)]
    for e in edges:
        graph.add_edge(e[0], e[1])

    print "Given the graph with edges %s" % graph.edges()
    print(
        "Breadth first traversal of gives us %s"
        % (graph.breadth_first_traversal(1))
    )
    print(
        "Depth first traversal gives us %s" %
        (graph.depth_first_traversal(1))
    )
