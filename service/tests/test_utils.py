import unittest
from service.utils import likes, time_online


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
        self.assertEqual(time_online(60), '1 минута')
        self.assertEqual(time_online(3600), '1 час')
        self.assertEqual(time_online(86400), '1 день')
        self.assertEqual(time_online(604800), '1 неделя')
        self.assertEqual(time_online(2592000), '1 месяц')
        self.assertEqual(time_online(31536000), '1 год')
        self.assertEqual(time_online(63), '1 минута и 3 секунды')
        self.assertEqual(time_online(87878), '1 день, 24 минут и 38 секунд')
        self.assertEqual(time_online(315365611), '10 лет, 1 час, 33 минут и 31 секунд')
        self.assertEqual(time_online(0), 'Сейчас')

    def test_display_time_exceptions(self):
        self.assertRaises(TypeError, time_online, 45.7)
        self.assertRaises(TypeError, time_online, {'seconds': 1})
        self.assertRaises(TypeError, time_online, ('minutes',))
        self.assertRaises(TypeError, time_online, {'1', '2', '3'})
