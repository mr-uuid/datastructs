import unittest
from datastructs.queue import Queue

class QueueTester(unittest.TestCase):
    def test_insert(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)

        self.assertEquals(
            [x.value for x in iter(q)],
            [1, 2, 3, 4, 5]
        )

        deq = q.dequeue()
        print deq
        assert deq == 1

        self.assertEquals(
            [x.value for x in iter(q)],
            [2, 3, 4, 5]
        )

if __name__ == "__main__":
    unittest.main()
