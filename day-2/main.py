from utils import *

totalValue = 0

with open("input.txt") as file: 
    lines = file.readlines()

    for line in lines:
        sequence = getSequence(line)
        if isSequencePossible(sequence):
            totalValue += getGameId(line)

print(totalValue)