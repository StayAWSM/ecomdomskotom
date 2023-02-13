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


def format_duration(seconds):
    if not isinstance(seconds, int):
        raise TypeError(f'method accepts only Int type. You tried to use {type(seconds)}.')
    intervals = (
        (31536000, ['год', 'года', 'лет']),  # 60 * 60 * 24 * 365
        (2592000, ['месяц', 'месяца', 'месяцев']),  # 60 * 60 * 24 * 30
        (604800, ['неделю', 'недели', 'недель']),  # 60 * 60 * 24 * 7
        (86400, ['день', 'дня', 'дней']),  # 60 * 60 * 24
        (3600, ['час', 'часа', 'часов']),  # 60 * 60
        (60, ['минуту', 'минуты', 'минут']),  # 60 sec
        (1, ['секунду', 'секунды', 'секунд']))  # one sec
    result = []

    for count, time_units in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value in [1, 21, 31, 41, 51]:
                time_units = time_units[0]
            elif 4 >= value >= 2:
                time_units = time_units[1]
            elif value >= 5:
                time_units = time_units[2]
            result.append(f'{value} {time_units}')

    from_years_to_hours = ', '.join(result[:-2])  # everything except minutes and seconds

    match len(result):
        case 0:
            return 'Сейчас'
        case 1:
            return f'{result[0]} назад'
        case 2:
            return f'{result[0]} и {result[1]} назад'
        case _:
            return f'{from_years_to_hours}, {result[-2]} и {result[-1]} назад'
