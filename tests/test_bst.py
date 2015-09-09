import unittest
from datastructs.tree import BinarySearchTree as tree


class BSTTester(unittest.TestCase):
	def test_insert(self):
		t = tree()
		t.insert(2)
		t.insert(1)
		t.insert(3)
		t.insert(5)
		t.insert(4)

		print [y.value for x, y in t.iter_preorder()]
		print [y.value for x, y in t.iter_postorder()]
		print [y.value for x, y in t.iter_inorder()]

	def test_insert2(self):
		t = tree()
		t.insert(1)
		t.insert(2)
		t.insert(3)
		t.insert(4)
		t.insert(5)

		print [y.value for x, y in t.iter_preorder()]
		print [y.value for x, y in t.iter_postorder()]
		print [y.value for x, y in t.iter_inorder()]

if __name__ == "__main__":
	unittest.main()
