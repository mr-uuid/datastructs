import unittest
from datastructs.linkedlist import LinkedList


class LLTester(unittest.TestCase):
	def test_init_append_and_extend(self):
		l = LinkedList.fromList([0,1,2,3,4])
		l.extend([5,6,7,8,9])
		self.assertEquals(
			[ x.value for x in list(l)],
			list(xrange(0,10))
		)

	def test_index(self):
		l = LinkedList.fromList([0,1,2,3,4])
		self.assertEquals(
			l.index(1),
			1
		)

	def test_pop(self):
		l = LinkedList.fromList([0,1,2,3,4])
		print [ x.value for x in list(l)],
		pval1 = l.pop(0)
		print pval1, [ x.value for x in list(l)],
		pval2 = l.pop(3)
		print pval2, [ x.value for x in list(l)],
		self.assertEquals(pval1, 0)
		self.assertEquals(pval2, 4)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,2,3]
		)

	def test_get(self):
		l = LinkedList.fromList([0,1,2,3,4])
		self.assertEquals(l.get(3), 3)
		self.assertEquals(l.get(1), 1)

	def test_remove(self):
		l = LinkedList.fromList([0,1,0,2,3,4])

		l.remove(0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,0,2,3,4]
		)

		l.remove(0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,2,3,4]
		)

		l.remove(3)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,2,4]
		)

	def test_insert(self):
		l = LinkedList.fromList([2])

		l.insert(1, 3)
		self.assertEquals(
			[ x.value for x in list(l)],
			[2,3]
		)

		l.insert(0, 0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[0,2,3]
		)

		l.insert(1, 1)
		self.assertEquals(
			[ x.value for x in list(l)],
			[0,1,2,3]
		)


	def test_remove_and_insert(self):
		l = LinkedList.fromList([0,1,0,2,3,4])

		l.remove(0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,0,2,3,4]
		)

		l.remove(0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,2,3,4]
		)

		l.remove(3)
		self.assertEquals(
			[ x.value for x in list(l)],
			[1,2,4]
		)

		l.remove(1)
		l.remove(4)

		l.insert(1, 3)
		self.assertEquals(
			[ x.value for x in list(l)],
			[2,3]
		)

		l.insert(0, 0)
		self.assertEquals(
			[ x.value for x in list(l)],
			[0,2,3]
		)

		l.insert(1, 1)
		self.assertEquals(
			[ x.value for x in list(l)],
			[0,1,2,3]
		)

if __name__ == "__main__":
	l = LinkedList()
	print l.length()
	unittest.main()
