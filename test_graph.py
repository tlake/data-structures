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


def test_add_node(create_graph):
    graph = create_graph
    #  graph.add_node()#  not sure what we are passing in yet


def test_add_edge(create_graph):
    graph = create_graph
    #  graph.add_edge()#  not sure what we are passing in yet


def test_del_node(create_graph):
    graph = create_graph
    #  we need to make/find a node here
    #  graph.del_node()#  not sure what we are passing in yet


def test_del_edge(create_graph):
    graph = create_graph
    #  graph.del_edge()#  not sure what we are passing in yet


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
