class ListNode(object):
    next = None
    prev = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        val = ""
        if self.prev:
            val += "{} <<-- ".format(self.prev.value)
        val += "{}".format(self.value)
        if self.next:
            val += " -->> {}".format(self.next.value)
        return val


class StackNode(object):
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        val = "{}".format(self.value)
        if self.next:
            val += ", next: {}".format(self.next.value)
        return val


class QueueNode(object):
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        val = "{}".format(self.value)
        if self.next:
            val += ", next: {}".format(self.next.value)
        return val


class GraphNode(object):
    value = None
    visited = False

    def __init__(self, value):
        self.value = value

    def __str__(self):
        val = "{}".format(self.value)
        return val

    def __repr__(self):
        return "<Node {}, visited: {}>".format(self.__str__(), self.visited)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    __lt__ = lambda self, obj: int(self) < int(obj)
    __le__ = lambda self, obj: int(self) <= int(obj)
    __eq__ = lambda self, obj: int(self) == int(obj)
    __ge__ = lambda self, obj: int(self) >= int(obj)
    __gt__ = lambda self, obj: int(self) > int(obj)
    __ne__ = lambda self, obj: int(self) != int(obj)
