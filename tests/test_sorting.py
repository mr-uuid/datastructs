import unittest
import importlib
import random
import time
import collections
import json

sorting_algos = ['insertion', 'merge', 'quick', 'selection']

class TestSorting(unittest.TestCase):
    def itterate_through_sorts(self, array_instantiator):
        for algo in sorting_algos:
            sort = getattr(importlib.import_module('algorithms.sorting.{}'.format(algo)), 'sort')
            my_sort, real_sort = sort(array_instantiator()), sorted(array_instantiator())
            print "algo: ", algo
            print "my sort: ", my_sort
            print "real sort: ", real_sort
            self.assertEquals(my_sort, real_sort)

    def test_empty(self):
        array = lambda : []
        self.itterate_through_sorts(array)

    def test_single(self):
        array = lambda: [-1]
        self.itterate_through_sorts(array)

    def test_even(self):
        array = lambda: [4, 2]
        self.itterate_through_sorts(array)

    def test_odd(self):
        array = lambda: [3, 1, 5]
        self.itterate_through_sorts(array)

    def test_negative(self):
        array = lambda: [12, 231, 1, -1, 212, -21, 1231, 1, -121231, 32, 32, 2]
        self.itterate_through_sorts(array)

    def test_string(self):
        array = lambda: list("The quick brown fox jumps over the lazy dog".replace(" ", "").lower())
        self.itterate_through_sorts(array)

    @unittest.SkipTest
    def test_benchmark(self):
        ns = [10, 100, 1000, 10000]
        random.seed(5)
        arrays = []
        for _ in xrange(10):
            arrays.append(lambda: [random.randint(-n, n) for x in xrange(n)])

        benchmark = collections.defaultdict(list)

        for n in ns:
            for array in arrays:
                for algo in sorting_algos:
                    before = time.time()
                    sort = getattr(importlib.import_module('algorithms.sorting.{}'.format(algo)), 'sort')
                    sort(array())
                    total = time.time() - before
                    benchmark[algo].append((n, total))

        with open('benchmark.json', 'w') as fh:
            fh.write(json.dumps(dict(benchmark), indent=2))

if __name__ == "__main__":
    unittest.main()
