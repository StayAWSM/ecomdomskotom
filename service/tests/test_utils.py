import unittest
from service.utils import likes, display_time


class TestLikes(unittest.TestCase):

    def test_likes(self):
        self.assertEqual(likes([]), 'No one likes this')
        self.assertEqual(likes(['Bob']), 'Bob likes this')
        self.assertEqual(likes(['Alex', 'Bob']), 'Alex and Bob like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John']), 'Artur, Bob and John like this')
        self.assertEqual(likes(['Artur', 'Bob', 'John', 'Liza']), 'Artur, Bob and 2 others like this')

    def test_likes_exceptions(self):
        self.assertRaises(TypeError, likes, 1)
        self.assertRaises(TypeError, likes, 45.7)
        self.assertRaises(TypeError, likes, {'Alex': 1})
        self.assertRaises(TypeError, likes, ('Bob', ))
        self.assertRaises(TypeError, likes, {'Alex', 'Bob', 'Alex'})


class TestDisplayTime(unittest.TestCase):
    def test_display_time(self):
        self.assertEqual(display_time(60), '1 минута')
        self.assertEqual(display_time(3600), '1 час')
        self.assertEqual(display_time(86400), '1 день')
        self.assertEqual(display_time(604800), '1 неделя')
        self.assertEqual(display_time(63), '1 минута 3 секунды')
        self.assertEqual(display_time(87878), '1 день 24 минут 38 секунд')
        self.assertEqual(display_time(0), 'Сейчас')

    def test_display_time_exceptions(self):
        self.assertRaises(TypeError, display_time, 45.7)
        self.assertRaises(TypeError, display_time, {'seconds': 1})
        self.assertRaises(TypeError, display_time, ('minutes',))
        self.assertRaises(TypeError, display_time, {'1', '2', '3'})
