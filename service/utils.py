def likes(names, lang='ru'):
    """
    A function that accepts an array of people
    and returns the corresponding text
    """
    if not isinstance(names, list):
        raise TypeError(f'method accepts only List type.'
                        f' You tried to use {type(names)}.')
    match len(names):
        case 0:
            return 'No one likes this' if lang == 'en' else 'Никому это не нравится'  # noqa pylint:disable=line-too-long
        case 1:
            return f'{names[0]} likes this' if lang == 'en' else f'{names[0]} оценил(а) это'  # noqa pylint:disable=line-too-long
        case 2:
            return f'{names[0]} and {names[1]} likes this' if lang == 'en' \
                else f'{names[0]} и {names[1]} оценили это'
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} likes this' \
                if lang == 'en' else \
                f'{names[0]}, {names[1]} и {names[2]} оценили это'
        case _:
            return f'{names[0]}, {names[1]} and {len(names) - 2} ' \
                f'others likes this' \
                if lang == 'en' else \
                f'{names[0]}, {names[1]} и {len(names) - 2} ' \
                f'других оценили это'


def _match_declensions(num):
    # берем последнюю цифру, так как от неё зависит склонение слова
    last_digit = int(str(num)[-1])
    if last_digit == 1 and num != 11:
        return 0  # склонение для единички и исключения в виде 11
    if (2 <= last_digit <= 4) and not (12 <= num <= 14):
        return 1  # для 2-4 и исключения 12-14
    return 2  # в иных случаях 3я форма


def format_duration(seconds, lang='ru'):
    if not isinstance(seconds, int):
        raise TypeError(f'method accepts only Int type.'
                        f' You tried to use {type(seconds)}.')

    intervals = (
        (31536000, ['год', 'года', 'лет', 'year', 'years']),
        (2592000, ['месяц', 'месяца', 'месяцев', 'month', 'months']),
        (604800, ['неделю', 'недели', 'недель', 'week', 'weeks']),
        (86400, ['день', 'дня', 'дней', 'day', 'days']),
        (3600, ['час', 'часа', 'часов', 'hour', 'hours']),
        (60, ['минуту', 'минуты', 'минут', 'minute', 'minutes']),
        (1, ['секунду', 'секунды', 'секунд', 'second', 'seconds']))
    result = []

    for count, declensions in intervals:
        value = seconds // count
        if value and lang == 'ru':
            result.append(f'{value} {declensions[_match_declensions(value)]}')
            seconds -= value * count
        elif value and lang == 'en':
            result.append(f'{value} {declensions[-1 if value > 1 else -2]}')
            seconds -= value * count

    # everything except minutes and seconds
    from_years_to_hours = ', '.join(result[:-2])

    match len(result):
        case 0:
            return 'Now' if lang == 'en' else 'Сейчас'
        case 1:
            return f'{result[0]} ago' if lang == 'en' \
                else f'{result[0]} назад'
        case 2:
            return f'{result[0]} and {result[1]} ago' \
                if lang == 'en' else f'{result[0]} и {result[1]} назад'
        case _:
            return f'{from_years_to_hours}, {result[-2]} and ' \
                   f'{result[-1]} ago'\
                if lang == 'en' else \
                   f'{from_years_to_hours}, {result[-2]} и {result[-1]} назад'
