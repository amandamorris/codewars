def get_sum(a,b):
    """Returns sum of numbers between a and b, inclusive"""
    # a and b are not ordered, so need to determine which one is smaller
    if a <= b:
        nums = range(a, b+1)
    else:
        nums = range(b, a+1)
    return sum(nums)
