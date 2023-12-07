from utils import *
import functools

processed_input: list[tuple] = []

with open("day-7/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        split_line = line.split()
        processed_input.append((split_line[0], int(split_line[1])))

sorted_list = sorted(processed_input, key=functools.cmp_to_key(hand_combination_sort))

total= 0

for i, t in enumerate(sorted_list):
    total += (i+1) * t[-1]

print (total)