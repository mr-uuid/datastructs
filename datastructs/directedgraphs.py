from collections import defaultdict
from nodes import GraphNode as Node
from queue import Queue
from stack import Stack


class Edge(object):
    weight = None
    src = None
    dst = None

    def __init__(self, n1, n2, weight=0):
        self.weight = weight
        self.src = n1
        self.dst = n2

    # def connects(self, n1, n2):
    #     return (self.src == n1 and self.dst == n2)

    def __repr__(self):
        return "<Edge {}>".format(str(self))
    def __str__(self):
        string = "{} --{}--> {}".format(self.src.value, self.weight,
                                        self.dst.value)
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
        """
        Inserts a node into the graph with the specified value
        """
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
            return None
        elif len(nodes) > 1:
            raise KeyError("Duplicate nodes for value {} detected".format(value))
        return nodes[0]

    def find_edge(self, src, dst):
        """
        Returns the edge associated between the src and the dst,
        if it exists.
        Params:
        :src: The id of the source node for the edge.
        :dst: The id of the destination node for the edge.
        """
        # Get all edges that satisfy that connect the src to the dst (should only be one)
        edges = [edge for edge in self.adjacents[src] if edge.dst.value == dst]
        if len(edges) == 0:
            return None
        elif len(edges) > 1:
            raise KeyError("Duplicate edges from {} to {} detected".format(src, dst))
        return edges[0]

    def insert_edge(self, src, dst):
        """
        Connects a Node with value: src to the Node with value: dst
        Params:
        :src: The id of the node that is the source of the edge
        :dst: The id of the node that is the destination of the edge
        """
        # Make sure edge doesn't already exists
        if self.find_edge(src, dst) is not None:
            return False
        n1, n2 = self.find_node(src), self.find_node(dst)
        self.adjacents[src].append(Edge(n1, n2))
        return True

    def neighbors(self, node):
        return [edge.dst for edge in self.adjacents[node.value]]

    def iterate_dfs(self, node, depth=None):
        """
        DFS traversal involves traversing a graph starting at a specified node.
        A node's adjacent nodes are traversed if they had not been traversed before.
        """
        if depth is None:
            for n in self.nodes:
                n.visited = False
            depth = 0

        node.visited = True
        yield depth, node

        for neighbor in self.neighbors(node):
            # import pdb;pdb.set_trace()
            if not neighbor.visited:
                for elem in self.iterate_dfs(neighbor, depth + 1):
                    yield elem

    def iterate_bfs(self, node, depth=None):
        """
        BFS traversal involves traversing a graph starting at a specified node.
        A node's adjacent nodes are traversed if they had not been traversed before.
        """
        if depth is None:
            for n in self.nodes:
                n.visited = False
            depth = 0

        if not node.visited:
            node.visited = True
            yield depth, node

        # Visit all the neighbors first
        node_stack = []
        for neighbor in self.neighbors(node):
            # import pdb;pdb.set_trace()
            if not neighbor.visited:
                neighbor.visited = True
                yield depth + 1, neighbor
                node_stack.append(neighbor)

        # Then continue to the next layer
        for item in node_stack:
            for elem in self.iterate_bfs(item, depth + 1):
                yield elem

    def iterate_edges_dfs(self, node, depth=None):
        """
        DFS traversal involves traversing a graph starting at a specified node.
        A node's adjacent nodes are traversed if they had not been traversed before.
        """
        if depth is None:
            for n in self.nodes:
                n.visited = False
            depth = 0

        node.visited = True

        for edge in self.adjacents[node.value]:
            # import pdb;pdb.set_trace()
            if not edge.dst.visited:
                edge.dst.visited = True
                yield depth + 1, edge
                for elem in self.iterate_edges_dfs(edge.dst, depth + 1):
                    yield elem

    def iterate_edges_bfs(self, node, depth=None):
        """
        BFS traversal involves traversing a graph starting at a specified node. It then traverses
        all neigbors before attempting to traverse the neighboring node for each neighbor.
        """
        if depth is None:
            for n in self.nodes:
                n.visited = False
            depth = 0

        if not node.visited:
            node.visited = True

        # Visit all the neighbors first
        node_stack = []
        for edge in self.adjacents[node.value]:
            # import pdb;pdb.set_trace()
            if not edge.dst.visited:
                edge.dst.visited = True
                yield depth + 1, edge
                node_stack.append(edge.dst)

        # Then continue to the next layer
        for item in node_stack:
            for elem in self.iterate_edges_bfs(item, depth + 1):
                yield elem

    def shortest_path(self, src, dst):
        for edge in


    def n(self):
        """
        Returns the # of nodes
        """
        return len(self.nodes)

    def e(self):
        """
        Returns the # of edges
        """
        return sum([len(x) for x in self.adjacents.values()])


    # def __repr__(self):
    #     return str([x.value for x in iter(self)])


    def __iter__(self):
        for v in self.nodes:
            yield v

if __name__ == "__main__":
    # Creates a Graph with nodes 0 - 4
    g = DirectedGraph.fromInt(4)
    print g.nodes

    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)
    g.insert_edge(1, 4)
    print g.e()

    print list(g.iterate_dfs(g.find_node(1)))
    print list(g.iterate_bfs(g.find_node(1)))
    print list(g.iterate_edges_dfs(g.find_node(1)))
    print list(g.iterate_edges_bfs(g.find_node(1)))
