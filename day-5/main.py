from utils import *

totalValue = 0

maps: dict = {}
seeds: list[int]

with open("day-5/input.txt") as f:
    lines = f.readlines()
    current_map: str
    for line in lines:
        if "seeds:" in line: 
            # part 1
            #seeds = list(map(int, line.split(":")[1].strip().split(" ")))
            # part 2
            seeds = parseSeedLine(list(map(int, line.split(":")[1].strip().split(" "))))

        elif "map:" in line: 
            fromToLabel = line.split(" ")[0].split("-to-")
            current_map = fromToLabel[0]
            maps[current_map] = {
                "to": fromToLabel[1],
                "exceptionMapping": []
            }
        elif not line.isspace():
            maps[current_map]["exceptionMapping"].append(line)


minLocation = -1
for seed in seeds:
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

print(minLocation)