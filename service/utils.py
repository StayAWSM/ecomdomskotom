def likes(names):
    """
    A function that accepts an array of people and returns the corresponding text

    WARNING: Operator match-case works with Python3.10+
    """
    if not isinstance(names, list):
        raise TypeError(f'method accepts only List type. You tried to use {type(names)}.')

    match len(names):
        case 0:
            return 'No one likes this'
        case 1:
            return f'{names[0]} likes this'
        case 2:
            return f'{names[0]} and {names[1]} like this'
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        case _:
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def display_time(seconds, granularity=3):  # granularity - number of values
    intervals = (
        ('неделя', 604800),  # 60 * 60 * 24 * 7
        ('день', 86400),  # 60 * 60 * 24
        ('час', 3600),  # 60 * 60
        ('минута', 60),
        ('секунда', 1),
    )
    result = []

    if not isinstance(seconds, int):
        raise TypeError(f'method accepts only Int type. You tried to use {type(seconds)}.')
    if seconds == 0:
        return 'Сейчас'

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if 2 <= value <= 4:
                match name:
                    case 'неделя':
                        name = 'недели'
                    case 'день':
                        name = 'дня'
                    case 'час':
                        name = 'часа'
                    case 'минута':
                        name = 'минуты'
                    case 'секунда':
                        name = 'секунды'
            elif value >= 5:
                match name:
                    case 'неделя':
                        name = 'недель'
                    case 'день':
                        name = 'дней'
                    case 'час':
                        name = 'часов'
                    case 'минута':
                        name = 'минут'
                    case 'секунда':
                        name = 'секунд'
            result.append("{} {}".format(value, name))
    return ' '.join(result[:granularity])
