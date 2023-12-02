from utils import *

totalValuePossibleGame = 0
totalPowerOfSets = 0

with open("input.txt") as file: 
    lines = file.readlines()

    for line in lines:
        sequence = getSequence(line)
        if isSequencePossible(sequence):
            totalValuePossibleGame += getGameId(line)
        
        minDiceRequired = getMinDiceRequired(sequence)
        power = 1
        for val in minDiceRequired.values():
            power *= val

        totalPowerOfSets += power

print(f"part 1: sum possible games: {totalValuePossibleGame}")
print(f"part 2: sum of power of set: {totalPowerOfSets}")
