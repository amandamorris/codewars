def anagrams(word, words):
    """Given a list of words, see return a list containing any that are anagrams
    of word"""

    alphaword = sorted(word)  # sort the chars of word
    anagrams = []  # empty list to store anagrams

    for string in words:  # iterate through each word
        if sorted(string) == alphaword:  # sort each word, compare with alphaword
            anagrams.append(string)  # if equal, append original string to list
    return anagrams
