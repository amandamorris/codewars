def array_diff(a, b):
    """Returns an array containing elements in a not in b"""
    #your code here
    difference = []
    for elem in a:
        if elem not in b:
            difference.append(elem)
    return difference
