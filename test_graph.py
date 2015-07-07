#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from graph import Graph


@pytest.fixture()
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


def test_nodes(create_graph):
    graph = create_graph
    for node in [1, 2, 3, 4, 5]:
        assert node in graph.nodes()


def test_edges(create_graph):
    graph = create_graph
    for edge in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        assert edge in graph.edges()


def test_add_node(create_graph):
    graph = create_graph
    graph.add_node(6)
    assert 6 in graph.nodes()
    graph.add_node(7, [1, 2, 3, 4, 5, 6])
    assert 7 in graph.nodes()


def test_add_edge(create_graph):
    """asserts that the edges we add are returned
    and that if a new node is added as an edge that
    node is added to the graph.
    """
    graph = create_graph
    graph.add_edge(5, 1)
    graph.add_edge(5, 6)
    edge_one = (5, 1)
    edge_two = (5, 6)
    assert edge_one in graph.edges()
    assert edge_two in graph.edges()
    assert 6 in graph.nodes()


def test_del_node(create_graph):
    """deletes an existing node and asserts that the node is
    no longer there and that its associated edges are also
    no longer there
    """
    graph = create_graph
    graph.del_node(1)
    assert 1 not in graph.nodes()
    assert (1, 2) not in graph.edges()


def test_del_edge(create_graph):
    """deletes an existing edge and make sure that the edge
    no longer exists but that the node itself still does.
    """
    graph = create_graph
    graph.del_edge(1, 2)
    assert (1, 2) not in graph.edges()
    assert 1 in graph.nodes()


def test_has_node(create_graph):
    graph = create_graph
    #  graph.has_node()#  not sure what we are passing in yet


def test_neighbors(create_graph):
    graph = create_graph
    #  we need to make/find a node here
    #  graph.has_node()#  not sure what we are passing in yet


def test_adjacent(create_graph):
    graph = create_graph
    #  we need to make/find 2 nodes here
    # graph.adjacent(node1, node2)
