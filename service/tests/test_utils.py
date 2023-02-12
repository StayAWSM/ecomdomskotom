import unittest
from service.utils import likes


class TestLikes(unittest.TestCase):

    def test_likes(self):
        self.assertEqual(likes([]), 'No one likes this')
        self.assertEqual(likes(['Bob']), 'Bob likes this')
        self.assertEqual(likes(['Alex', 'Bob']), 'Alex and Bob like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John']),
                         'Artur, Bob and John like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John', 'Liza']),
                         'Artur, Bob and 2 others like this')

    def test_likes_exceptions(self):
        self.assertRaises(TypeError, likes, 1)
        self.assertRaises(TypeError, likes, 45.7)
        self.assertRaises(TypeError, likes, {'Alex': 1})
        self.assertRaises(TypeError, likes, ('Bob', ))
        self.assertRaises(TypeError, likes, {'Alex', 'Bob', 'Nikolay'})
