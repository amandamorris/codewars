def get_middle(s):
    """Returns the middle char(s) of the input string"""
    length = len(s)
    if length %2 ==1:
        return s[length/2]
    else:
        return s[length/2-1:length/2+1]
