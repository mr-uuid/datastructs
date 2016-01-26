from node import ListNode as Node
from collections import defaultdict

class Vertex(object):
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        val = "{}".format(self.value)
        return val


class Edge(object):
    weight = None
    directed = False
    start = None
    stop = None

    def __init__(self, n1, n2, weight=None, directed=False):
        self.start = n1
        self.stop = n2
        self.weight = weight
        self.directed = directed

    def connects(self, n1, n2):
        if self.directed:
            return self.start is n1 and self.stop is n2
        return (self.start is n1 and self.stop is n2) or (self.start is n2 and
                                                          self.stop is n1)

class Graph(list):
    edges = defaultdict(list)
    vertexes = []

    def add_vertex(self, value):
        self.vertexes.append(Vertex(value))

    def find_vertex(self, value):
        for v in self.vertexes:
            if v.value == value:
                return v
            print v
        return None

    def add_edge(self, value1, value2):
        v1, v2 = self.find_vertex(value1), self.find_vertex(value2)
        if v1 is None:
            raise ValueError("Node with value {} not found.".format(value1))
        if v2 is None:
            raise ValueError("Node with value {} not found.".format(value2))

        self.edges[value1].append(Edge(v1, v2))
        self.edges[value2].append(Edge(v2, v1))

    def num_of_vertexes(self):
        return len(self.vertexes)

    def num_of_edges(self):
        return sum([len(x) for x in self.edges.values()])

    # def dfs(self, vertex):
    #     """
    #     Returns a depth first search of the graph starting from the given vertex
    #     """

    # def bfs(self, vertex):
    #     """
    #     Returns a depth first search of the graph starting from the given vertex
    #     """

    # def __repr__(self):
    #     return str([x.value for x in iter(self)])


    def __iter__(self):
        for v in self.vertexes:
            yield v

if __name__ == "__main__":
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)

    g.add_edge(1, 4)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print g.num_of_edges()
