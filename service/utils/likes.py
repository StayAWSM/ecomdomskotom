def likes(names):

    if not names:
        return 'No one likes this'

    elif sum(names) == 1:
        return f'{names[0]} likes this'

    elif sum(names) == 2:
        return f'{names[0]} and {names[1]} likes this'

    elif sum(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} likes this'

    else:
        return f'{names[0]}, {names[1]} and {sum(names)-2} others likes this'