def likes(names):
    """A function that accepts an array of people and returns the corresponding text"""
    match len(names):
        case 0:
            return 'No one likes this'
        case 1:
            return f'{names[0]} likes this'
        case 2:
            return f'{names[0]} and {names[1]} likes this'
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} likes this'

    if len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others likes this'
