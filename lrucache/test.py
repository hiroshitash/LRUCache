import unittest

from lrucache import LRUCache, lrucache_decorator

class LRUCacheTests(unittest.TestCase):

    def setUp(self):
        self.counter = 0    # used in test_decorator

    def tearDown(self):
        pass


    def test_size3(self):
        cache = LRUCache(3)
        cache.put(1,'One')
        cache.put(2,'Two')
        cache.put(3,'Three')
        cache.put(2,'Two')
        cache.put(1,'One')
        cache.put(4,'Four')

        self.assertTrue( cache.get(1) == 'One' )
        self.assertTrue( cache.get(2) == 'Two' )
        self.assertTrue( cache.get(4) == 'Four' )
        self.assertTrue( cache.get(3) == None )

    def test_differntVals(self):
        cache = LRUCache()
        cache.put(1,'One')
        cache.put(2,'Two')
        cache.put(3,'Three')
        cache.put(2,2)
        cache.put(1,1)
        cache.put(4,'Four')

        self.assertTrue( cache.get(1) == 1 )
        self.assertTrue( cache.get(2) == 2 )
        self.assertTrue( cache.get(3) == 'Three' )
        self.assertTrue( cache.get(4) == 'Four' )


    def test_size3_default_minus_1(self):
        cache = LRUCache(3, -1)
        self.assertTrue( cache.get(3) == -1 )


    @lrucache_decorator(3, None)
    def fake_func1(self, key):
        self.counter += 1
        return "%s_%s" % (key, self.counter)

    def test_decorator_with_args(self):
        self.assertEqual(self.fake_func1(1), "1_1")
        self.assertEqual(self.fake_func1(1), "1_1")
        self.assertEqual(self.fake_func1(2), "2_2")
        self.assertEqual(self.fake_func1(3), "3_3")
        self.assertEqual(self.fake_func1(4), "4_4")
        self.assertEqual(self.fake_func1(1), "1_5")


    @lrucache_decorator(3, -1)
    def fake_func2(self, key):
        self.counter += 1
        return "%s_%s" % (key, self.counter)

    def test_decorator_size3_with_args(self):
        self.assertEqual(self.fake_func2(1), "1_1")
        self.assertEqual(self.fake_func2(2), "2_2")
        self.assertEqual(self.fake_func2(3), "3_3")
        self.assertEqual(self.fake_func2(2), "2_2")
        self.assertEqual(self.fake_func2(1), "1_1")
        self.assertEqual(self.fake_func2(4), "4_4")
        self.assertEqual(self.fake_func2(3), "3_5")


    @lrucache_decorator()
    def fake_func3(self, key):
        self.counter += 1
        return "%s_%s" % (key, self.counter)

    def test_decorator_with_no_args(self):
        self.assertEqual(self.fake_func3(1), "1_1")
        self.assertEqual(self.fake_func3(1), "1_1")
        self.assertEqual(self.fake_func3(2), "2_2")
        self.assertEqual(self.fake_func3(3), "3_3")
        self.assertEqual(self.fake_func3(4), "4_4")
        self.assertEqual(self.fake_func3(1), "1_1")  # cache size is bigger with no arg


if __name__ == '__main__':
    unittest.main()
