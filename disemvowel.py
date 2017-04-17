def disemvowel(string):
    """removes vowels from string"""
    newstring = ""
    for char in string:
        if char not in set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
            newstring += char

    return newstring
