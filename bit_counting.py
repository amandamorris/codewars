def countBits(n):
    """Returns the number of 1s in the binary representation of n"""
    binary = "{0:b}".format(n)  # convert n to binary representation (string)
    return binary.count("1")  # return number of "1"s in binary representation
