from utils import *

items: list[dict[str, int]] = []
flows: dict[str, Flow] = {}

with open("day-19/input.txt") as file: 
    processItem = False
    for line in file.readlines():
        if line.isspace():
            processItem = True
        elif processItem: 
            items.append(parseItem(line))
        else: 
            flow = parseFlow(line)
            flows[flow.getName()] = flow
        
assert("in" in flows)

startingFlow = 'in'

totalSum = 0

for item in items:
    action = startingFlow
    while action not in ['A', 'R']:
        action = flows[action].processItem(item)

    if action == 'A':
        totalSum += sum(item.values())

print(f"total sum of accepted items: {totalSum}")