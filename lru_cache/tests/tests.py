from unittest import TestCase
from src.main import cached, set_cache_key, get_cache_key


class LruCacheTests(TestCase):

    def setUp(self):
        self.assertEqual(len(cached), 0)

    def tearDown(self):
        for key in cached.keys():
            cached.pop(key)

    def test_can_set_value(self):
        key, value = 'test', 123
        cached_value = set_cache_key(key, value)

        self.assertEqual(len(cached), 1)
        self.assertIn(key, cached)
        self.assertEqual(cached[key], value)
        self.assertEqual(value, cached_value)

        new_value = 456
        cached_value = set_cache_key(key, new_value)
        self.assertEqual(len(cached), 1)
        self.assertIn(key, cached)
        self.assertEqual(cached[key], new_value)
        self.assertEqual(new_value, cached_value)

    def test_can_get_value(self):
        key, value = 'test', 123
        saved_value = set_cache_key(key, value)
        cached_value = get_cache_key(key)

        self.assertEqual(saved_value, cached_value)
        self.assertEqual(saved_value, value)
        self.assertEqual(value, cached_value)

    def test_can_get_value_from_database(self):
        key = 'test'
        cached_value = get_cache_key(key)
        self.assertIn(key, cached_value)

    def test_lru_sort(self):
        first, value = 'first', 123
        set_cache_key(first, value)
        second, value = 'second', 456
        set_cache_key(second, value)

        keys = cached.keys()
        self.assertEqual(keys.index(first), 0)
        self.assertEqual(keys.index(second), 1)

        get_cache_key(first)
        keys = cached.keys()
        self.assertEqual(keys.index(first), 1)
        self.assertEqual(keys.index(second), 0)

        third, value = 'third', 789
        set_cache_key(third, value)
        keys = cached.keys()
        self.assertEqual(keys.index(first), 0)
        self.assertEqual(keys.index(third), 1)

    def test_max_size(self):
        to_be_cached = {'a': 1, 'b': 3, 'c': 2}
        for key, value in to_be_cached.items():
            set_cache_key(key, value)

        self.assertEqual(len(cached), 2)
        self.assertNotIn('a', cached)
        self.assertIn('b', cached)
        self.assertIn('c', cached)
