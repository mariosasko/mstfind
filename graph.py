from typing import Hashable
from constants import Edge

class Graph:

    def __init__(self):
        self._vertices = set()
        self._edges = set()
        self._vertex_neighbours = {}

    def add_vertex(self, vertex: Hashable):
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            self._vertex_neighbours[vertex] = set()

    def remove_vertex(self, vertex: Hashable):
        self._vertices.remove(vertex)
        for v, w in self._vertex_neighbours[vertex]:
            self._vertex_neighbours[v].remove((vertex, w))
        del self._vertex_neighbours[vertex]

        for (u, v), w in self._edges.copy():
            if u == vertex or v == vertex:
                self._edges.remove(((u, v), w))

    def add_edge(self, edge: Edge, weight=1):
        u, v = edge

        if ((v, u), weight) in self._edges:
            return
        
        self._edges.add(((u, v), weight))

        self.add_vertex(u)
        self.add_vertex(v)

        self._vertex_neighbours[u].add((v, weight))
        self._vertex_neighbours[v].add((u, weight))
    
    def remove_edge(self, edge: Edge, weight=1):
        u, v = edge
        self._vertex_neighbours[u].remove((v, weight))
        self._vertex_neighbours[v].remove((u, weight))

        if ((u, v), weight) in self._edges: 
            self._edges.remove(((u, v), weight))
        else:
            self._edges.remove(((v, u), weight))

    def vertices(self):
        return self._vertices.copy()

    def edges(self):
        return self._edges.copy()
    
    def vertex_neighbours(self, vertex: Hashable):
        return self._vertex_neighbours[vertex]