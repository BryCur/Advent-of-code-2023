from utils import *
import functools

directionSequence: str
nodeMap : dict = {}

with open("day-8/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if not line.isspace():
            if "=" in line : 
                input = line.split(" = ")
                nodeMap[input[0]] = process_input_tuple(input[1])
            else: 
                directionSequence = line.strip()

startingNode = "AAA"
step_count = 0
currentNode = startingNode
while currentNode != "ZZZ":
    currentNode = getNextStep(nodeMap, currentNode, directionSequence[step_count%len(directionSequence)])
    step_count += 1
    #print(currentNode)

print(f"Part 1 - step from AAA to ZZZ: {step_count}")
