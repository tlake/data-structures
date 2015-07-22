#!/usr/bin/env python

from __future__ import unicode_literals
import pytest
from data_structures.graph import Graph


@pytest.fixture()
def create_graph():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5]
    edges = [
        (1, 2, 1), (2, 3, 2),
        (3, 4, 3), (4, 5, 6)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        # node1, node2, weight
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def create_graph2():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5]
    edges = [
        (1, 3, 2), (1, 4, 2), (2, 4, 3),
        (2, 5, 4), (3, 2, 1)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def create_graph3():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5]
    edges = [
        (1, 3, 1), (1, 2, 2), (3, 6, 3),
        (2, 4, 2), (4, 5, 1)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def cyclical_graph():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5, 6, 7]
    edges = [
        (1, 2, 3), (2, 3, 3), (3, 5, 2),
        (5, 4, 2), (5, 6, 1), (4, 2, 1),
        (4, 7, 1)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def create_spaghetti():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    edges = [
        (1, 2, 3), (1, 3, 2), (1, 4, 5),
        (2, 9, 5), (2, 5, 3), (2, 6, 1),
        (3, 5, 5), (3, 7, 5), (4, 6, 6),
        (4, 8, 2), (5, 9, 3), (6, 9, 5),
        (7, 8, 5), (4, 7, 1)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def create_dijk():
    graph = Graph()
    nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    edges = [
        (1, 2, 2), (2, 11, 2), (2, 12, 1), (2, 7, 1),
        (1, 3, 3), (3, 10, 3), (3, 8, 1), (3, 9, 3),
        (9, 8, 1), (1, 4, 1), (4, 7, 3), (4, 6, 1),
        (4, 5, 2), (6, 7, 2)
    ]
    for n in nodes:
        graph.add_node(n)
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


@pytest.fixture()
def create_negative():
    graph = Graph()
    nodes = [1, 2, 3, 4, 'a', 'b', 'c']
    edges = [
        (1, 'c', -1), (1, 'b', -2),
        (2, 'c', -2),
        (3, 'a', -5), (3, 1, -9),
        ('c', 1, 1), ('c', 2, 3),
        ('b', 3, -7)]
    for e in edges:
        graph.add_edge(e[0], e[1], e[2])
    return graph


def test_nodes(create_graph):
    graph = create_graph
    for node in [1, 2, 3, 4, 5]:
        assert node in graph.nodes()


def test_edges(create_graph):
    graph = create_graph
    for edge in [
        (1, 2), (2, 3),
        (3, 4), (4, 5)
    ]:
        assert edge in graph.edges()


def test_add_node(create_graph):
    graph = create_graph
    graph.add_node(6)
    assert 6 in graph.nodes()


def test_add_edge(create_graph):
    """asserts that the edges we add are returned
    and that if a new node is added as an edge that
    node is added to the graph.
    """
    graph = create_graph
    graph.add_edge(5, 1, 3)
    graph.add_edge(5, 6, 4)
    edge_one = (5, 1)
    edge_two = (5, 6)
    added_node = 6
    assert edge_one in graph.edges()
    assert edge_two in graph.edges()
    assert added_node in graph.nodes()


def test_del_node(create_graph):
    """deletes an existing node and asserts that the node is
    no longer there and that its associated edges are also
    no longer there.  Also makes sure the appropriate error
    is raised if the node is not there.
    """
    graph = create_graph
    graph.add_edge(2, 1, 5)
    graph.del_node(1)
    assert 1 not in graph.nodes()
    assert (1, 2) not in graph.edges()
    assert (2, 1) not in graph.edges()
    with pytest.raises(IndexError):
        graph.del_node(7)


def test_del_edge(create_graph):
    """deletes an existing edge and make sure that the edge
    no longer exists but that the node itself still does.
    """
    graph = create_graph
    graph.del_edge(1, 2)
    assert (1, 2) not in graph.edges()
    assert 1 in graph.nodes()
    with pytest.raises(IndexError):
        graph.del_edge(1, 5)


def test_has_node(create_graph):
    """
    .has_node() should return True if the node exists in the
    graph, or return False if it does not exist in the graph.
    """
    graph = create_graph
    assert not graph.has_node(8)
    assert graph.has_node(2)
    graph.add_node(177)
    assert graph.has_node(177)
    graph.del_node(2)
    assert not graph.has_node(2)


def test_neighbors(create_graph):
    """
    .neighbors() should return a list of all nodes connected
    by edges to the given node. It should raise an error if
    the given node does not exist in the graph.
    """
    graph = create_graph
    assert 2 in graph.neighbors(1)
    assert 4 not in graph.neighbors(1)
    graph.add_edge(1, 3, 0)
    graph.add_edge(1, 4, 2)
    assert 3 in graph.neighbors(1)
    assert 4 in graph.neighbors(1)
    graph.del_edge(1, 3)
    assert 3 not in graph.neighbors(1)
    with pytest.raises(KeyError):
        graph.neighbors(88)


def test_adjacent(create_graph):
    """
    .adjacent() should return True if the first node is pointing
    to the second node, or False if it is not. If either of the
    given nodes do not exist in the graph, it should raise a
    KeyError.
    """
    graph = create_graph
    assert graph.adjacent(1, 2)
    assert not graph.adjacent(2, 1)
    with pytest.raises(KeyError):
        graph.adjacent(6, 5)
    with pytest.raises(KeyError):
        graph.adjacent(5, 6)


def test_depth_first_traversal(create_graph, create_graph2, cyclical_graph):
    graph1 = create_graph
    graph2 = create_graph2
    c_graph = cyclical_graph
    assert graph1.depth_first_traversal(1) == [1, 2, 3, 4, 5]
    assert graph2.depth_first_traversal(1) == [1, 3, 2, 4, 5]
    assert graph1.depth_first_traversal(2) == [2, 3, 4, 5]
    assert graph2.depth_first_traversal(2) == [2, 4, 5]
    assert graph1.depth_first_traversal(3) == [3, 4, 5]
    assert graph2.depth_first_traversal(3) == [3, 2, 4, 5]
    assert c_graph.depth_first_traversal(1) == [1, 2, 3, 5, 4, 7, 6]


def test_breadth_first_traversal(
    create_graph, create_graph2, create_graph3,
    cyclical_graph, create_spaghetti
):
    graph1 = create_graph
    assert graph1.breadth_first_traversal(1) == [1, 2, 3, 4, 5]
    assert graph1.breadth_first_traversal(2) == [2, 3, 4, 5]
    assert graph1.breadth_first_traversal(3) == [3, 4, 5]

    graph2 = create_graph2
    assert graph2.breadth_first_traversal(1) == [1, 3, 4, 2, 5]
    assert graph2.breadth_first_traversal(3) == [3, 2, 4, 5]
    assert graph2.breadth_first_traversal(4) == [4]

    c_graph = cyclical_graph
    assert c_graph.breadth_first_traversal(1) == [1, 2, 3, 5, 4, 6, 7]

    graph3 = create_graph3
    assert graph3.breadth_first_traversal(1) == [1, 2, 3, 4, 6, 5]

    spag = create_spaghetti
    t1_nodes = [1]
    t2_nodes = [2, 3, 4]
    t3_nodes = [6, 9, 5, 7, 8]
    bft_vals = spag.breadth_first_traversal(1)
    assert bft_vals[0] in t1_nodes
    for ndx in [1, 2, 3]:
        assert bft_vals[ndx] in t2_nodes
    for ndx in [4, 5, 6, 7, 8]:
        assert bft_vals[ndx] in t3_nodes


def test_dijkstra(create_dijk, create_spaghetti):
    graph = create_dijk
    dijk_vals = graph.dijkstra(1)
    # total weight of node 7 should be 3
    assert dijk_vals[0][7] == 3
    # total weight of node 8 should be 4
    assert dijk_vals[0][8] == 4
    # prev node of node 7 should be node 2
    assert dijk_vals[1][7] == 2
    # prev node of node 8 should be node 3
    assert dijk_vals[1][8] == 3

    spag = create_spaghetti
    spag_vals = spag.dijkstra(1)
    # total weight of node 9 should be 8
    assert spag_vals[0][9] == 8
    # total weight of node 8 should be 7
    assert spag_vals[0][8] == 7
    # total weight of node 6 should be 4
    assert spag_vals[0][6] == 4
    # prev node of node 9 should be 2
    assert spag_vals[1][9] == 2
    # prev node of node 8 should be 4
    assert spag_vals[1][8] == 4
    # prev node of node 6 should be 2
    assert spag_vals[1][6] == 2


def test_bellman(create_graph, create_graph2, create_negative, create_graph3,
                 cyclical_graph, create_spaghetti, create_dijk):
    assert create_graph.BellmanFord(1) == ({1: 0, 2: 1, 3: 3, 4: 6, 5: 12},
                                           {2: 1, 3: 2, 4: 3, 5: 4})
    assert create_graph2.BellmanFord(1) == ({1: 0, 2: 3, 3: 2, 4: 2, 5: 7},
                                            {2: 3, 3: 1, 4: 1, 5: 2})
    assert create_graph3.BellmanFord(1) == ({1: 0, 2: 2, 3: 1, 4: 4, 5: 5, 6: 4},
                                            {2: 1, 3: 1, 4: 2, 5: 4, 6: 3})
    assert cyclical_graph.BellmanFord(1) == (
        {1: 0, 2: 3, 3: 6, 4: 10, 5: 8, 6: 9, 7: 11},
        {2: 1, 3: 2, 4: 5, 5: 3, 6: 5, 7: 4})
    assert create_spaghetti.BellmanFord(1) == (
        {1: 0, 2: 3, 3: 2, 4: 5, 5: 6, 6: 4, 7: 6, 8: 7, 9: 8},
        {2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 4, 8: 4, 9: 2})
    print create_dijk.BellmanFord(1) == (
        {1: 0, 2: 2, 3: 3, 4: 1, 5: 3, 6: 2, 7: 3, 8: 4, 9: 6, 10: 6, 11: 4, 12: 3},
        {2: 1, 3: 1, 4: 1, 5: 4, 6: 4, 7: 2, 8: 3, 9: 3, 10: 3, 11: 2, 12: 2})

    with pytest.raises(ValueError):
        create_negative.BellmanFord(1)
