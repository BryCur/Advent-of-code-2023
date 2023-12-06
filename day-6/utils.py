

def getMinPushtimetoWin(maxtime: int, goalDistance: int):
    for t in range(maxtime):
        if t * (maxtime-t) > goalDistance:
            return t
        
    return 0


def getMaxPushtimetoWin(maxtime: int, goalDistance: int):
    for t in range(maxtime, 0, -1):
        if t * (maxtime-t) > goalDistance:
            return t
        
    return 0