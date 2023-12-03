from utils import *

matrix = []

with open("day-3/input.txt") as f:
    matrix = f.readlines()

currX= 0
currY = 0
totalValue = 0
while True:
    currX, currY = findNextSupportedSymbolInMatrix(matrix, currX, currY)

    if currY == -1 and currX == -1:
        break

    numberPositions = getAdjacentNumberPositionsFrom(matrix, currX, currY)

    for pos in numberPositions:
            totalValue += consumeNumberAtPosition(matrix, *pos)

    
    currY += 1

print(totalValue)