def find_missing(sequence):
    """"sequence is an arithmetic progression that skips one term.  This function
    identifies the skipped term.
    Ex: findMissing([1,3,5,9,11]) == 7
    """
    differences = {}  # dictionary to keep track of difference between
                      # consecutive terms.  keys will be difference, values will
                      # be list of index tuples with that difference

    for i in range(len(sequence) - 1):  # iterate through indices in sequence
        diff = sequence[i + 1] - sequence[i]  # calculate difference between consec terms
        differences.setdefault(diff, [])  # set default [] dict value for key diff
        differences[diff].append((i, i+1))  # append indices to value list

    for difference in differences:  # check values of 2 keys in dictionary
        indices = differences[difference]
        if len(indices) == 1:  # if length of the list is 1, this will give us
                               # indices relating to skipped term
            return sequence[indices[0][0]] + difference/2  # return skipped term