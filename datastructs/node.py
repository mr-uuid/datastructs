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

