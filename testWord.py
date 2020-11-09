from word import Word
import unittest

class testWord(unittest.TestCase):
    def setUp(self):
        self.str1 = 'apple'
        self.str2 = 'fig'
        self.str3 = 'boats'
        self.word1 = Word(self.str1)
        self.word2 = Word(self.str2)
        self.word3 = Word(self.str3)
        
    def test_gt(self):
        self.assertNotEqual(self.str1 > self.str2, self.word1 > self.word2)

    def test_ge(self):
        self.assertTrue(self.word1 >= self.word3)

    def test_lt(self):
        self.assertNotEqual(self.str2 < self.str1, self.word2 < self.word1)

    def test_le(self):
        self.assertTrue(self.word1 <= self.word3)

unittest.main()
