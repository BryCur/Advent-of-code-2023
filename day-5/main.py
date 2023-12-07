from utils import *

totalValue = 0

maps: dict = {}
seed_input: list[int]

with open("day-5/input.txt") as f:
    lines = f.readlines()
    current_map: str
    for line in lines:
        if "seeds:" in line: 
            seed_input = list(map(int, line.split(":")[1].strip().split(" ")))

        elif "map:" in line: 
            fromToLabel = line.split(" ")[0].split("-to-")
            current_map = fromToLabel[0]
            maps[current_map] = {
                "to": fromToLabel[1],
                "exceptionMapping": []
            }
        elif not line.isspace():
            maps[current_map]["exceptionMapping"].append(line)


# part 1
minLocation = -1
for seed in seed_input:
    currentResourceKey = "seed"
    currentNumber = seed
    while currentResourceKey in maps:
        exceptions = maps[currentResourceKey]["exceptionMapping"]

        resultFromException = isNumberInExceptionMapping(exceptions, currentNumber)
        currentNumber = resultFromException if resultFromException >= 0 else currentNumber
        currentResourceKey = maps[currentResourceKey]["to"]

        if currentResourceKey == "location" and minLocation != -1:
            minLocation = min(currentNumber, minLocation)
        elif currentResourceKey == "location":
            minLocation = currentNumber

print(f"part 1 - min location: {minLocation}")


#part 2
minLocation = -1
seed_input_copy = seed_input.copy()
while len(seed_input_copy) > 2:
    seedRangeSize = seed_input_copy.pop()
    seedRangeStart = seed_input_copy.pop()
    
    currentResourceKey = "seed"
    currentranges: list = [(seedRangeStart, seedRangeSize)]
    while currentResourceKey in maps:
        exceptions = maps[currentResourceKey]["exceptionMapping"]
        
        nextRanges = []
        for range in currentranges:
            current_exceptions, toExcludeFrom = getMatchingRangeToExceptionMapping(exceptions, range)
            regular_range = excludeRangesFromRange(toExcludeFrom, range)
            currentranges = current_exceptions + regular_range
            
        currentResourceKey = maps[currentResourceKey]["to"]

        if currentResourceKey == "location" and minLocation != -1:
            minLocation = min(sorted(currentranges)[0][0], minLocation)
        elif currentResourceKey == "location":
            minLocation = sorted(currentranges)[0][0]