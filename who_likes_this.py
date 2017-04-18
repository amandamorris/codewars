def likes(names):
    """Returns text describing the names that like a post"""
    length = len(names)

    if not names:
        return "no one likes this"

    elif length == 1:
        return "%s likes this" % (names[0])

    elif length == 2:
        return "%s and %s like this" % (names[0], names[1])

    elif length == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])

    else:
        num_others = length - 2
        return "%s, %s and %d others like this" % (names[0], names[1], num_others)