import unittest
from datastructs.graphs import Graph

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(1, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

class GraphTester(unittest.TestCase):
    def test_reads(self):
        self.assertEquals(
            [x.value for x in g.vertexes],
            [1, 2, 3, 4]
        )

        self.assertEquals(
            len(g.edges),
            4,
        )

if __name__ == "__main__":
    unittest.main()
