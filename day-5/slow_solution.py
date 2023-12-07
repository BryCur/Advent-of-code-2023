from utils import *

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

print("finished parsing input")

#part 2
minLocation = -1
OFFSET_MAX_STEP = 10000000
seed_input_copy = seed_input.copy()
while len(seed_input_copy) > 2:
    seedRangeSize = seed_input_copy.pop()
    seedRangeStart = seed_input_copy.pop()
    seedRangeStop = seedRangeStart + seedRangeSize

    print(f"SEED INPUT PAIR ------ processing input pair of seed; remaining {len(seed_input_copy)} of {len(seed_input)}")

    for offset in range((seedRangeSize % OFFSET_MAX_STEP) + 1):

        start_seed = seedRangeStart + offset * OFFSET_MAX_STEP
        stop_seed = min(start_seed + OFFSET_MAX_STEP, seedRangeStop)

        range_to_process = list(range(start_seed, stop_seed))
        print(f"processing range {offset} of {len(range_to_process)}")

        for seed in range_to_process: 
            currentResourceKey = "seed"
            currentNumber = seed
            while currentResourceKey in maps:
                exceptions = maps[currentResourceKey]["exceptionMapping"]

                # meets the range in exception0
                resultFromException = isNumberInExceptionMapping(exceptions, currentNumber)
                currentNumber = resultFromException if resultFromException >= 0 else currentNumber

                currentResourceKey = maps[currentResourceKey]["to"]

                if currentResourceKey == "location" and minLocation != -1:
                    minLocation = min(currentNumber, minLocation)
                elif currentResourceKey == "location":
                    minLocation = currentNumber
        
        print(f"min location for processed range: {minLocation}")