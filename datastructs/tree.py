# from node import TreeNode as Node
import collections


class BinarySearchTreeNode(object):
    """
    A node within a binary search tree.
    """
    value = None
    right_children = None
    left_children = None

    def __init__(self, value):
        self.value = value
        self.right_children = []
        self.left_children = []

    def is_leaf(self):
        return not self.has_right_children() and not self.has_left_children()

    def has_right_children(self):
        return len(self.right_children) > 0

    def has_left_children(self):
        return len(self.left_children) > 0

    def children(self):
        return self.left_children + self.right_children


Node = BinarySearchTreeNode


class BinarySearchTree(object):
    """
    A basic implementation of a binary search tree.
    """
    root = None
    children = []

    def insert(self, value):
        """
        Inserts a node into the binary search tree.
        """
        # If Tree is empty
        if self.root is None:
            self.root = Node(value)
            return

        self._insert(self.root, value)

    def _insert(self, node, value):
        """
        A recursive insert function.
        """
        if node.value == value:
            print "Node is already in array."
            return 

        if value > node.value:
            if node.has_right_children():
                self._insert(node.right_children[0], value)
            else:
                node.right_children.append(Node(value))
        elif value < node.value:
            if node.has_left_children():
                self._insert(node.left_children[0], value)
            else:
                node.left_children.append(Node(value))

    # SEE IF THERE IS A DECORATOR THAT MAPS CLASS ATTR FUNCTIONS TO A FUNCTION BEING CALLED WITH A CERTAIN VAR
    # @map(_iter_preorder, "preorder")

    # Each of the following methods generates an itterator for the tree nodes.
    iter_preorder = lambda self: self.iter('preorder')
    iter_postorder = lambda self: self.iter('postorder')
    iter_inorder = lambda self: self.iter('inorder')

    def iter(self, order):
        """
        Iterates over the tree in the given order style.
        """
        mapping = {
            "preorder": self._iter_preorder,
            "postorder": self._iter_postorder,
            "inorder": self._iter_inorder,
        }
        func = mapping.get(order, None)
        if not func:
            raise ValueError("Invalid Iteration Order: {}".format(order))
        if self.root is None:
            return []
        return func(self.root)

    def _iter_preorder(self, node, layer=0):
        """
        An iterator where the node is given before its children.
        The traversal defaults to nodes with the least value (left first).
        Note to self: Pre order gave back the same order as insertion
        """
        # if node is None:
        #     yield StopIteration()
        # Yield node first
        yield layer, node
        # ... Then children, left to right
        for child in node.children():
            for item in self._iter_preorder(child, layer+1):
                yield item      

    def _iter_postorder(self, node, layer=0):
        """
        A nodes children are visited before the node itself.
        The traversal defaults to nodes with the least value (left first).
        """
        # Base Case: No more nodes left
        # if node is None:
        #     yield StopIteration()
        # Yield children first, from left to right
        for child in node.children():
            for item in self._iter_postorder(child, layer+1):
                yield item
        # ... Then Node
        yield layer, node

    def _iter_inorder(self, node, layer=0):
        """
        A nodes left children are visited then the node, then the nodes right children
        The traversal defaults to nodes with the least value (left first).
        """
        # if node is None:
        #     yield StopIteration()
        # Yield left children
        for child in node.left_children:
            for item in self._iter_postorder(child, layer+1):
                yield item
        # ... Then Node
        yield layer, node
        # ... Then right children
        for child in node.right_children:
            for item in self._iter_postorder(child, layer+1):
                yield item

    def __iter__(self):
        return self.pre_order_map(lambda x: x.value)

    def __str__(self):
        string = ""
        for layer, node in self.iter("preorder"):
            string += "{}{}\n".format("  "*layer, node.value)
        return string
        
# make a balanced binary search tree!
