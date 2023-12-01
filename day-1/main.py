
from utils import *

totalValue: int = 0

with open('input.txt') as file: 
    lines: list[str] = file.readlines()
    for line in lines: 
        sequence = exctractDigits(line)
        val = getValueFromSequence(sequence)

        totalValue += val

print(totalValue)