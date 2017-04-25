def fibonacci(n):
    """Returns the nth fibonacci number, works for large n"""
    fibs = [0, 1]  # start with first two numbers, stored in fibs

    for i in range(2, n+1):  # for each successive number
        fibs.append(fibs[i-1]+fibs[i-2])  # add 2 previous, append to fibs

    return fibs[n]
