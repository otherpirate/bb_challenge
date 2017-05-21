from unittest import TestCase
from src.main import find_anagrams


class FindAnagramsTests(TestCase):

    def test_find_anagram(self):
        word = 'Eat'
        anagrams = ['Coffee', 'Tea', 'Water']
        find = find_anagrams(word, anagrams)
        self.assertEqual(len(find), 1)
        self.assertIn('Tea', anagrams)

    def test_not_find_anagram(self):
        word = 'Jedi'
        anagrams = ['Coffee', 'Death', 'Star']
        find = find_anagrams(word, anagrams)
        self.assertEqual(len(find), 0)
