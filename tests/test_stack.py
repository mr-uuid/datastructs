import unittest
from datastructs.stack import Stack

class BSTTester(unittest.TestCase):
    def test_insert(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        self.assertEquals(
            [x.value for x in iter(stack)],
            [5, 4, 3, 2, 1]
        )

        pop = stack.pop()
        print pop
        assert pop == 5

        self.assertEquals(
            [x.value for x in iter(stack)],
            [4, 3, 2, 1]
        )

if __name__ == "__main__":
    unittest.main()
