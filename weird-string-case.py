def to_weird_case(string):
    """Within a word, even indexes are uppercased, odd indexes are lowercased"""
    weird_cased = ""
    index = 0
    for char in string:
        if not char.isalpha():
            weird_cased += char
            index = 0
            continue
        if index % 2 == 0:
            weird_cased += char.upper()
            index += 1
        else:
            weird_cased += char.lower()
            index += 1
    return weird_cased
