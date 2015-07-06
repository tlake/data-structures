#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from graph import Graph

def create_graph():
    graph = Graph()
    return graph

def test_nodes(create_graph):
    graph = create_graph
    nodes = graph.nodes()
    #  assert nodes == [1, 2, 3, 4, 5]


def test_edges(create_graph):
    graph = create_graph
    edges = graph.edges()
    #  assert edges == ???


def test_add_node():
    pass


def test_add_edge():
    pass


def test_del_node():
    pass


def test_del_edge():
    pass


def test_has_node():
    pass


def test_neighbors():
    pass


def test_adjacent():
    pass
