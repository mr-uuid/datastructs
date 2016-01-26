from nodes import StackNode as Node

class Stack(object):
    top = None

    @classmethod
    def fromList(cls, _list):
        """
        Create a Stack from a List
        """
        elem = cls()
        for item in _list:
            elem.push(item)
        return elem

    def push(self, value):
        """
        Pushes an element to the top of the stack
        """

        if self.top is None:
            self.top = Node(value)
            return

        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise KeyError("Can not pop. Stack is empty.")
        val = self.top.value
        self.top = self.top.next
        return val

    def length(self):
        length = 0
        node = self.top
        while node is not None:
            node = node.next
            length += 1
        return length

    def __nonzero__(self) :
        return self.length() > 0

    def __repr__(self):
        return str(list(reversed([x.value for x in iter(self)])))

    def __iter__(self):
        current = self.top
        while current is not None:
            yield current
            current = current.next
