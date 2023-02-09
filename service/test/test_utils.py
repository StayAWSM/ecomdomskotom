import unittest
from service.utils.likes import likes


class TestLikes(unittest.TestCase):

    def test_values(self):
        self.assertEqual(likes([]), 'No one likes this')
        self.assertEqual(likes(['Bob']), 'Bob likes this')
        self.assertEqual(likes(['Alex', 'Bob']), 'Alex and Bob like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John']), 'Artur, Bob and John like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John', 'Liza']), 'Artur, Bob and 2 others like this')

    def test_raise(self):
        self.assertRaises(TypeError, likes, 1)
        self.assertRaises(TypeError, likes, 45.7)
        self.assertRaises(TypeError, likes, 2)
        self.assertRaises(TypeError, likes, ('Bob', ))
