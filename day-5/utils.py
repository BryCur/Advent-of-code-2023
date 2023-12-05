import collections

def isNumberInExceptionMapping(exceptions: list[str], number: int) -> int:
    for line in exceptions:
        fromToRangeInt: list[int] = list(map(int, line.split()))

        if isNumberInRange(number, fromToRangeInt[1], fromToRangeInt[2]):
            return fromToRangeInt[0] + (number - fromToRangeInt[1])
    
    return -1


def isNumberInRange(number: int, start:int, range:int) -> bool: 
    return number >= start and number < start + range

def parseSeedLine(values: list[int])-> list[int]:
    startRange: int = 0
    finalList = []
    for i, val in enumerate(values):
        if i % 2 == 0: # start of range
            startRange = val
        else:
            finalList.extend(range(startRange, startRange+val))

    return finalList