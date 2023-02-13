import unittest
from service.utils import likes, format_duration


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
        self.assertEqual(format_duration(1), '1 секунду')
        self.assertEqual(format_duration(60), '1 минуту')
        self.assertEqual(format_duration(3600), '1 час')
        self.assertEqual(format_duration(86400), '1 день')
        self.assertEqual(format_duration(604800), '1 неделю')
        self.assertEqual(format_duration(2592000), '1 месяц')
        self.assertEqual(format_duration(31536000), '1 год')
        self.assertEqual(format_duration(63), '1 минуту и 3 секунды')
        self.assertEqual(format_duration(87878), '1 день, 24 минут и 38 секунд')
        self.assertEqual(format_duration(315365611), '10 лет, 1 час, 33 минут и 31 секунд')
        self.assertEqual(format_duration(0), 'Сейчас')

    def test_display_time_exceptions(self):
        self.assertRaises(TypeError, format_duration, 45.7)
        self.assertRaises(TypeError, format_duration, {'seconds': 1})
        self.assertRaises(TypeError, format_duration, ('minutes',))
        self.assertRaises(TypeError, format_duration, {'1', '2', '3'})
