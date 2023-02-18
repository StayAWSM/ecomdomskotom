import unittest
from service.utils import likes, format_duration


class TestLikes(unittest.TestCase):

    def test_likes(self):
        self.assertEqual(likes([], lang='en'), 'No one likes this')
        self.assertEqual(likes(['Bob'], lang='en'), 'Bob likes this')
        self.assertEqual(likes(['Максим', 'Ольга']), 'Максим и Ольга оценили это')  # noqa pylint:disable=line-too-long
        self.assertEqual(likes(['Максим', 'Ольга', 'John']), 'Максим, Ольга и John оценили это')  # noqa pylint:disable=line-too-long
        self.assertEqual(likes(['Максим', 'Ольга', 'Никита', 'Alex'], lang='en'),  # noqa pylint:disable=line-too-long
                         'Максим, Ольга and 2 others likes this')
        self.assertEqual(likes(['Artur', 'Bob', 'Richard'], lang='en'),
                         'Artur, Bob and Richard likes this')

    def test_likes_exceptions(self):
        self.assertRaises(TypeError, likes, 1)
        self.assertRaises(TypeError, likes, 45.7)
        self.assertRaises(TypeError, likes, {'Alex': 1})
        self.assertRaises(TypeError, likes, ('Bob', ))
        self.assertRaises(TypeError, likes, {'Alex', 'Bob', 'Alica'})


class TestDisplayTime(unittest.TestCase):
    """A simple method showing user activity"""

    def test_format_duration(self):
        # for ru lang
        self.assertEqual(format_duration(0), 'Сейчас')
        self.assertEqual(format_duration(1), '1 секунду назад')
        self.assertEqual(format_duration(60), '1 минуту назад')
        self.assertEqual(format_duration(3600), '1 час назад')
        self.assertEqual(format_duration(86400), '1 день назад')
        self.assertEqual(format_duration(63), '1 минуту и 3 секунды назад')
        self.assertEqual(format_duration(87878), '1 день, 24 минуты и 38 секунд назад')  # noqa pylint:disable=line-too-long
        self.assertEqual(format_duration(315365611), '10 лет, 1 час, 33 минуты и 31 секунду назад')  # noqa pylint:disable=line-too-long
        self.assertEqual(format_duration(81), '1 минуту и 21 секунду назад')
        self.assertEqual(format_duration(736302), '1 неделю, 1 день, 12 часов, 31 минуту и 42 секунды назад')  # noqa pylint:disable=line-too-long

        # for en lang
        self.assertEqual(format_duration(0, lang='en'), 'Now')
        self.assertEqual(format_duration(1, lang='en'), '1 second ago')
        self.assertEqual(format_duration(60, lang='en'), '1 minute ago')
        self.assertEqual(format_duration(3600, lang='en'), '1 hour ago')
        self.assertEqual(format_duration(87878, lang='en'),
                         '1 day, 24 minutes and 38 seconds ago')
        self.assertEqual(format_duration(315365611, lang='en'),
                         '10 years, 1 hour, 33 minutes and 31 seconds ago')
        self.assertEqual(format_duration(81, lang='en'), '1 minute and 21 seconds ago')  # noqa pylint:disable=line-too-long
        self.assertEqual(format_duration(736302, lang='en'), '1 week, 1 day, 12 hours, 31 minutes and 42 seconds ago')  # noqa pylint:disable=line-too-long

    def test_format_duration_exceptions(self):
        self.assertRaises(TypeError, format_duration, 45.7)
        self.assertRaises(TypeError, format_duration, {'seconds': 1})
        self.assertRaises(TypeError, format_duration, ('minutes',))
        self.assertRaises(TypeError, format_duration, {'1', '2', '3'})
