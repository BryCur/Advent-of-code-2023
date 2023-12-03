from utils import *

PUZZLE_PART = 2

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

    if PUZZLE_PART == 1:
        for pos in numberPositions:
                totalValue += consumeAndReturnNumberAtPosition(matrix, *pos)
    if PUZZLE_PART == 2:
         if countAllUniqueNumberAroundPos(matrix, currX, currY) == 2 and matrix[currX][currY] == "*":
                product = 1
                for pos in numberPositions:
                    number_at_pos = consumeAndReturnNumberAtPosition(matrix, *pos)
                    product *= number_at_pos if number_at_pos != 0 else 1
                totalValue += product



    
    currY += 1

print(totalValue)