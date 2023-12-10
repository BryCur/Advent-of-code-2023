from utils import *
import math

directionSequence: str
nodeMap : dict = {}

PART_SELECTOR = 2

with open("day-8/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if not line.isspace():
            if "=" in line : 
                input = line.split(" = ")
                nodeMap[input[0]] = process_input_tuple(input[1])
            else: 
                directionSequence = line.strip()

if PART_SELECTOR == 1:
    startingNode = "AAA"
    step_count = 0
    currentNode = startingNode
    while currentNode != "ZZZ":
        currentNode = getNextStep(nodeMap, currentNode, directionSequence[step_count%len(directionSequence)])
        step_count += 1
        #print(currentNode)

    print(f"Part 1 - step from AAA to ZZZ: {step_count}")

else: 
    startingNodes = [ key for key in nodeMap.keys() if key[-1] == 'A']
    step_count = 0
    currentNodes = startingNodes

    print(f"depart nodes: {currentNodes}")
    starting_map = { x: [] for x in currentNodes }
    _shouldContinue = True
    LENGTH_STOP = 1
    
    while _shouldContinue: #(currentNodes):
        nextNodes = []
        for node in currentNodes:
            next_node = getNextStep(nodeMap, node, directionSequence[step_count%len(directionSequence)])
            if next_node[-1] == "Z":
                start_node = startingNodes[currentNodes.index(node)]

                arrival = Arrival(next_node, step_count+1, 0 if len(starting_map[start_node]) < 1 else starting_map[start_node][-1].totalStepRequired, step_count%len(directionSequence))
                starting_map[start_node].append(arrival)

                for item in starting_map.values():
                    if len(item) < LENGTH_STOP:
                        _shouldContinue = True
                        break
                    else: 
                        _shouldContinue = False

            nextNodes.append(next_node)
        
        step_count += 1
        currentNodes = nextNodes

    required_steps_for_starts = []
    for key, val in starting_map.items():
        required_steps_for_starts.append(val[-1].relativeStepRequired)
        print(f"Starting node {key} : {val}")

    
    print(required_steps_for_starts)
    required_steps = math.lcm(*required_steps_for_starts)

    print(f"Part 2 - step from A to Z: {required_steps}")
