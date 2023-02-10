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
