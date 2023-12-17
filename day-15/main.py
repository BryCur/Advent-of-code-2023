from utils import *
import itertools


maxBoxesIndex = 256
words: list[str] = []
boxes: list[list[tuple[str,int]]] = [None] * maxBoxesIndex

with open("day-15/input.txt") as file:
    words = file.readline().strip().split(",")

total_value = 0

for word in words:
    if '-' in word:
        label = word[:-1]
        box_index = HASH_algorithm_for_string(label)

        if boxes[box_index] is None:
            boxes[box_index] = []

        lense_index = find_lens_index(boxes[box_index], label)
        if lense_index != None:
            boxes[box_index].pop(lense_index)
    else:
        label, fLength = word.split('=')
        box_index = HASH_algorithm_for_string(label)

        if boxes[box_index] is None:
            boxes[box_index] = []
        
        lense_index = find_lens_index(boxes[box_index], label)
        if lense_index != None:
            boxes[box_index][lense_index] = (label, int(fLength))
        else: 
            boxes[box_index].append((label, int(fLength)))

    total_value += HASH_algorithm_for_string(word)

print(f"Part 1 - total value: {total_value}")



total_value = 0
for i, box in enumerate(boxes):
    if box is None:
        continue

    for j, (lense, fl) in enumerate(box):
        total_value += (i+1) * (j+1) * fl

print(f"Part 2 - total focusing power: {total_value}")