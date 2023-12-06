from utils import *
import functools

totalValue = 0

maps: dict = {}
seed_input: list[int]

input_timeList: list = []
input_distanceList: list = []

with open("day-6/input.txt") as f:
    lines = f.readlines()
    for line in lines: 
        label, value = line.split(":")
        if label == "Time":
            input_timeList = value.split()
        if label == "Distance":
            input_distanceList = value.split()


if len(input_timeList) != len(input_distanceList):
    print("asymetrical lists in input")
    exit()

#part 1
result = 1
timeList = list(map(int, input_timeList))
distanceList = list(map(int, input_distanceList))

if len(timeList) != len(distanceList):
    print("asymetrical lists for part 1")
    exit()

for raceIndex in range(len(timeList)):
    minTime = getMinPushtimetoWin(timeList[raceIndex], distanceList[raceIndex])
    maxTime = getMaxPushtimetoWin(timeList[raceIndex], distanceList[raceIndex])

    waysToWin = (maxTime - minTime) +1
    result *= waysToWin

print(f"part 1 - ways to win: {result}")


# part 2
maxTime = int(functools.reduce(lambda a,b: a+b, input_timeList))
maxDistance = int(functools.reduce(lambda a,b: a+b, input_distanceList))

minTime = getMinPushtimetoWin(maxTime, maxDistance)
maxTime = getMaxPushtimetoWin(maxTime, maxDistance)

waysToWin = (maxTime - minTime) +1

print(f"part 2 - ways to win: {waysToWin}")