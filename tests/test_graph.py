import unittest

from graph import Graph


class Placeholder:
    pass

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(('A', 'B'), 10)
        self.graph.add_edge(('A', 'C'), 2)
        self.graph.add_edge(('B', 'C'), 2)
    
    def test_remove_vertex(self):
        self.graph.remove_vertex('A')
        self.assertFalse('A' in self.graph.vertices())
        v_num = len([Placeholder for v, _ in set().union(*self.graph._vertex_neighbours.values()) 
                     if v == 'A'])
        self.assertEqual(v_num, 0)
        self.assertRaises(KeyError, self.graph.vertex_neighbours, 'A')
        vedge_num = len([Placeholder for ((u, v), _) in self.graph.edges() 
                         if u == 'A' or v == 'A'])
        self.assertEqual(vedge_num, 0)

    def test_remove_edge(self):
        self.graph.remove_edge(('A', 'B'), 10)
        self.assertFalse(('B', 10) in self.graph.vertex_neighbours('A'))
        self.assertFalse(('A', 10) in self.graph.vertex_neighbours('B'))
        self.assertFalse((('A', 'B'), 10) in self.graph.edges())
        self.assertFalse((('B', 'A'), 10) in self.graph.edges())
        self.assertRaises(KeyError, self.graph.remove_edge, ('B', 'C'), 10)
