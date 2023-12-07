import collections

def isNumberInExceptionMapping(exceptions: list[str], number: int) -> int:
    for line in exceptions:
        fromToRangeInt: list[int] = list(map(int, line.split()))

        if isNumberInRange(number, fromToRangeInt[1], fromToRangeInt[2]):
            return fromToRangeInt[0] + (number - fromToRangeInt[1])
    
    return -1


def isNumberInRange(number: int, start:int, range:int) -> bool: 
    return number >= start and number < start + range


def getMatchingRangeToExceptionMapping(exceptions: list[str], fromRange: (int, int)) -> list:
    exception_to = []
    exceptions_from = []
    for line in exceptions:
        fromToRangeInt: list[int] = list(map(int, line.split()))

        exceptionRangeFrom = getCrossInRange(fromRange, (fromToRangeInt[1], fromToRangeInt[2]))
        if exceptionRangeFrom != None:
            exception_to.append((fromToRangeInt[0] + abs(exceptionRangeFrom[0] - fromRange[1]), exceptionRangeFrom[1]))
            exceptions_from.append(exceptionRangeFrom)
    
    return exception_to, exceptions_from


def getCrossInRange(range1: (int, int), range2:(int, int)) -> tuple: 
    if range1 == range2: # ranges are the same
        return range1
    
    if range1[0] > sum(range2) or sum(range1) < range2[0]: # range 1 and 2 does not cross
        return None
    
    minStart = max(range1[0], range2[0])
    
    return (minStart, min(abs(sum(range1) - minStart), abs(sum(range2) - minStart)))

def excludeRangesFromRange(toExclude: list[(int, int)], baserange: (int, int)) -> list[(int, int)]:
    toExclude.sort()
    regular_range= []
    currMin = baserange[1]
    for exception in toExclude:
        if exception[0] == currMin:
            currMin = sum(exception)
        else:
            regular_range.append( (currMin, abs(exception[0] - currMin)))

    return regular_range