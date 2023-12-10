from utils import *
import functools

directionSequence: str
nodeMap : dict = {}

PART_SELECTOR = 2
input: list[list[int]] = []

with open("day-9/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        input.append(list(map(int,line.strip().split())))

total_value_next_in_sequence = 0
total_value_previous_in_sequence = 0
for seq in input:
    total_value_next_in_sequence += getNextNumberInSequence(seq)
    total_value_previous_in_sequence += getPreviousNumberInSequence(seq)

print(f"total value of next number in sequences: {total_value_next_in_sequence}")
print(f"total value of previous number in sequences: {total_value_previous_in_sequence}")


