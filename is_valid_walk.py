def isValidWalk(walk):
    #determine if walk takes exactly 10 minutes (1 min per block)
    location = [0,0]  # start at (0,0)
    time = 0  # (start at time=0)
    
    for direction in walk:
        time += 1  # always increment time
        if direction == "n":  # if north, increment y coordinate by 1
            location[1] += 1
        elif direction == "s":  # if south, decrement y coordinate by 1
            location[1] -= 1
        elif direction == "e":  # if east, increment x coordinate by 1
            location[0] += 1
        elif direction == "w":  # if west, decrement x coordinate by 1
            location[0] -= 1
        # location is final location - may not be (0,0) - need to factor in time to get back
        time += abs(location[0]) + abs(location[1])
        
        if time == 10:
            return True
        else:
            return False
