#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from graph import Graph


def create_graph():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    return graph


def test_nodes():
    graph = create_graph()
    for node in [1, 2, 3, 4, 5]:
        assert node in graph.nodes()


def test_edges():
    graph = create_graph()
    for edge in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        assert edge in graph.edges()
