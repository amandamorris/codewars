def digital_root(n):
    """Calls get_sum repeatedly as long as n > 9"""
    if n < 10:
        return n

    total = get_sum(n)
    while total > 9:
        total = get_sum(total)
    return total

def get_sum(n):
    """"Returns sum of digits of n"""
    nstr = str(n)
    summation = 0
    for char in nstr:
        summation = summation + int(char)
    return summation
