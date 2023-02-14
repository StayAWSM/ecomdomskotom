from translate import Translator


def likes(names, lang='ru'):
    """
    A function that accepts an array of people
    and returns the corresponding text
    """
    if not isinstance(names, list):
        raise TypeError(f'method accepts only List type.'
                        f' You tried to use {type(names)}.')

    if lang == 'en':
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
                return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'  # noqa pylint:disable=line-too-long
    else:
        match len(names):
            case 0:
                return f'Никому не нравится это'
            case 1:
                return f'{names[0]} нравится это'
            case 2:
                return f'{names[0]} и {names[1]} нравится это'
            case 3:
                return f'{names[0]}, {names[1]} и {names[2]} нравится это'
            case _:
                return f'{names[0]}, {names[1]} и {len(names) - 2} другим нравится это'  # noqa pylint:disable=line-too-long


def _match_declensions(num):
    last_digit = int(str(num)[-1])  # берем последнюю цифру, так как от неё зависит склонение слова
    if last_digit == 1 and num != 11:
        return 0  # склонение для единички и исключения в виде 11
    if (2 <= last_digit <= 4) and not (12 <= num <= 14):
        return 1  # для 2-4 и исключения 12-14
    return 2  # в иных случаях 3я форма


def format_duration(seconds, lang='ru'):
    if not isinstance(seconds, int):
        raise TypeError(f'method accepts only Int type.'
                        f' You tried to use {type(seconds)}.')

    translator = Translator(from_lang='ru', to_lang='en')

    intervals = (
        (31536000, ['год', 'года', 'лет']),  # 60 * 60 * 24 * 365
        (2592000, ['месяц', 'месяца', 'месяцев']),  # 60 * 60 * 24 * 30
        (604800, ['неделю', 'недели', 'недель']),  # 60 * 60 * 24 * 7
        (86400, ['день', 'дня', 'дней']),  # 60 * 60 * 24
        (3600, ['час', 'часа', 'часов']),  # 60 * 60
        (60, ['минуту', 'минуты', 'минут']),  # 60 sec
        (1, ['секунду', 'секунды', 'секунд']))  # one sec
    result = []

    for count, declensions in intervals:
        value = seconds // count
        if value:
            result.append(f'{value} {declensions[_match_declensions(value)]}')
            seconds -= value * count

    from_years_to_hours = ', '.join(result[:-2])  # everything except minutes and seconds

    if lang == 'en':
        match len(result):
            case 0:
                return translator.translate('Сейчас')
            case 1:
                return translator.translate(f'{result[0]} назад')
            case 2:
                return translator.translate(f'{result[0]} и {result[1]} назад')
            case _:
                return translator.translate(f'{from_years_to_hours}, {result[-2]} и {result[-1]} назад')
    else:
        match len(result):
            case 0:
                return 'Сейчас'
            case 1:
                return f'{result[0]} назад'
            case 2:
                return f'{result[0]} и {result[1]} назад'
            case _:
                return f'{from_years_to_hours}, {result[-2]} и {result[-1]} назад'
