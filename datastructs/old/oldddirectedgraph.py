from nodes import GraphNode as Node
from collections import defaultdict


class DirectedGraph(object):
    nodes = []
    adjacents = defaultdict(list)

    # @classmethod
    # def fromFile(cls, filename):

    @classmethod
    def fromInt(cls, integer):
        graph = cls()
        for x in xrange(1, integer+1):
            graph.insert_node(x)
        return graph

    def insert_node(self, value):
        node = self.find_node(value)
        if node is not None:
            raise KeyError("Node {} already exists.".format())
        node = Node(value)
        self.nodes.append(node)
        return node

    def find_node(self, value):
        """
        Returns the Node associated with the value
        Params:
        :value: an int containing the value of a Node
        """
        nodes = [n for n in self.nodes if n.value == value]
        if len(nodes) == 0:
            # raise KeyError("Value {} not found in graph.".format(value))
            return None
        elif len(nodes) > 1:
            raise KeyError("Duplicate nodes for value {} detected".format(value))
        return nodes[0]

    def find_edge(self, source, destination):
        """
        Returns the edge associated between the source and the destination,
        if it exists. Source and destination are nodes in the graph.
        :source: A node in the graph
        :destination: A node in the graph
        """
        # # Make sure the source and destination nodes exist:
        # if source.value not in self.adjacents or destination.value not in self.adjacents:
        #     return None

        # Get all edges that satisfy that connect the source to the destination (should only be one)
        edges = [edge for edge in self.adjacents[source.value]
                 if edge.destination.value == destination]

        if len(edges) == 0:
            # raise KeyError("Edge from {} to {} not found in graph.".format(
            #                source, destination))
            return None
        elif len(edges) > 1:
            raise KeyError("Duplicate edges from {} to {} detected".format(
                           source, destination))
        return edges[0]

    def insert_edge(self, source, destination):
        """
        Connects a Node with value: source to the Node with value: destination
        Params:
        :source: An Int containing the value of the source of the edge.
        :destination: An Int containing the value of the destination of the edge.
        """
        # Make sure edge doesn't already exists
        if self.find_edge(source, destination) is not None:
            return False

        self.adjacents[source].append(Edge(n1, n2))
        self.adjacents[destination].append(Edge(n2, n1))
        return True

        # source_node, destination_node = source, destination
        # if isinstance(source, int):
        #     source_node = self.find_node(source)
        #     if source_node is None:
        #         raise ValueError("Node with value {} not found.".format(source))

        # if isinstance(source, int):
        #     destination_node = self.find_node(destination)
        #     if destination_node is None:
        #         raise ValueError("Node with value {} not found.".format(destination))



    def neighbors(self, node):


    def num_of_nodes(self):
        return len(self.nodes)

    def num_of_edges(self):
        return sum([len(x) for x in self.adjacents.values()])

    def dfs(self, node):
        """
        DFS traversal involves traversing a graph starting at a specified node.
        A node's adjacent nodes are traversed if they had not been traversed before.
        """
        for n in self.nodes:
            n.visited = False

        self.find_node

    def _dfs(self, node):
        """
        DFS traversal involves traversing a graph starting at a specified node.
        A node's adjacent nodes are traversed if they had not been traversed before.
        """
        node.visited = True
        for adj in self.adjacents[node.value]:
            if not adj.visited:
                adj.visited = True
                self.dfs()

    # def bfs(self, vertex):
    #     """
    #     Returns a depth first search of the graph starting from the given vertex
    #     """

    # def __repr__(self):
    #     return str([x.value for x in iter(self)])


    def __iter__(self):
        for v in self.nodes:
            yield v


class Edge(object):
    weight = None
    source = None
    destination = None

    def __init__(self, n1, n2, weight=0):
        self.weight = weight
        self.source = n1
        self.destination = n2

    # def connects(self, n1, n2):
    #     return (self.source == n1 and self.destination == n2)

    def __str__(self):
        string = "{} --{}--> {}".format(self.source.value, self.weight,
                                        self.destination.value)
        return string

    def __int__(self):
        return int(self.weight)

    def __float__(self):
        return float(self.weight)

    __lt__ = lambda self, obj: int(self) < int(obj)
    __le__ = lambda self, obj: int(self) <= int(obj)
    __eq__ = lambda self, obj: int(self) == int(obj)
    __ge__ = lambda self, obj: int(self) >= int(obj)
    __gt__ = lambda self, obj: int(self) > int(obj)
    __ne__ = lambda self, obj: int(self) != int(obj)


if __name__ == "__main__":
    g = DirectedGraph.fromInt(4)
    print g.nodes

    g.insert_edge(1, 4)
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)

    print g.num_of_edges()
