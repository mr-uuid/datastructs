from nodes import ListNode as Node

class LinkedList(list):
    head = tail = None

    def __init__(self, _list=None):
        if _list:
            for item in _list:
                self.append(item)

    @classmethod
    def fromList(cls, array):
        """
        Create a Linked Lists from a Python List
        """
        elem = cls()
        for item in array:
            elem.append(item)
        return elem

    def append(self, value):
        """
        Append a value from the array
        """
        # First Insert Ever
        if self.head is None:
            self.head = self.tail = Node(value)
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def extend(self, array):
        for item in array:
            self.append(item)

    def insert(self, index, value):
        # Inserting at the beginning of the list
        if index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        # We need to create any additional nodes needed
        if index > self.length():
            create = self.length() - index
            for x in xrange(0, create):
                self.append(None)

        node = Node(value)

        # If we are inserting at the tail
        if index == self.length():
            self.tail = node

        # Inserting at the specified index
        oldnode = self._get(index-1)
        node.next = oldnode.next
        oldnode.next = node


    def index(self, val):
        for ind, item in enumerate(iter(self)):
            if item.value == val:
                return ind
        raise IndexError("Value {} not found.".format(val))

    def remove(self, val):
        ind = self.index(val)
        self.pop(ind)

    def pop(self, index=None):
        if index is None:
            self.pop(self.length() - 1)

        # If popping the head
        if index == 0:
            val = self.head.value
            # Meaning only 1 element in the list, after we remove it, there will be none
            if self.tail is self.head:
                self.tail = self.head = None
                return val
            self.head = self.head.next
            return val

        # Find the node to be popped, and the value before it
        itterator = iter(self)
        for x in xrange(index):
            before = itterator.next()
        popme = itterator.next()

        if popme is self.tail:
            self.tail = before

        # Do the poping
        before.next = popme.next
        return popme.value

    def _get(self, index):
        if index >= self.length():
            raise IndexError("Index {} is out of range.".format(index))

        itterator = iter(self)
        for x in xrange(0, index):
            itterator.next()

        return itterator.next()

    def get(self, index):
        return self._get(index).value

    def length(self):
        return len(list(self))

    # WHAT IS LISTS DEFAULT REPR METHOD?
    # IMPLEMENT SORT
    # IMPLEMENT REVERSED
    def __repr__(self):
        return str([x.value for x in iter(self)])

    def __iter__(self):
        temphead = self.head
        while temphead is not None:
            yield temphead
            temphead = temphead.next
