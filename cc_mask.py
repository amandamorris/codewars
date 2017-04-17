# return masked string
def maskify(cc):
    """returns string with all but last 4 characters displaying as '#'"""
    length = len(cc)
    if length < 4:
        return cc
    else:
        num_hashes = length - 4

    return "#"*num_hashes + cc[num_hashes:]
