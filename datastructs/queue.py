from nodes import QueueNode as Node

class Queue(object):
    """
    A queue is a fifo implementation.
    Queue.enqueue(1)
    [1]
    Queue.enqueue(2)
    [2, 1]
    Queue.enqueue(3)
    [3, 2, 1]

    Queue.dequeue() -> 1
    [3, 2] -
    Queue.dequeue() -> 2
    [3]
    Queue.dequeue() -> 3
    []
    Queue.dequeue() -> raises IndexError
    """

    front = back = None

    @classmethod
    def fromList(cls, array):
        """
        Create a Queue from a Python List
        """
        elem = cls()
        for item in array:
            elem.enqueue(item)
        return elem

    def enqueue(self, value):
        """
        Inserts an element into the queue
        """

        if self.front is None:
            self.front = Node(value)
            self.back = self.front
            return

        self.back.next = Node(value)
        self.back = self.back.next

    def dequeue(self):
        """
        Removes an element from the queue
        """

        if self.front is None:
            raise IndexError("Can not dequeue. Queue is empty.")

        val = self.front.value
        self.front = self.front.next
        return val

    def length(self):
        length = 0
        node = self.front
        while node is not None:
            node = node.next
            length += 1
        return length

    def __nonzero__(self) :
        return self.length() > 0

    def __repr__(self):
        return str([x.value for x in iter(self)])

    def __iter__(self):
        current = self.front
        while current is not None:
            yield current
            current = current.next
