from utils import *
from itertools import combinations

galaxy_map: list[list[str]]=  []
with open("day-11/input.txt", 'r') as f:
    for line in f.readlines():
        galaxy_map.append([*line.strip()])

LINE_ADDITIONAL_WEIGHT = 1000000-1
COL_ADDITIONAL_WEIGHT = 1000000-1

DOUBLE_LINE_CHAR = "="
DOUBLE_COL_CHAR = "∥" 
DOUBLE_INTERSECTION_CHAR = "⊫"

# replacing lines are easier
for i, line in enumerate(galaxy_map):
    if len(set(line)) == 1 and line[0] == ".":
        for j in range(len(line)):
            galaxy_map[i][j] = DOUBLE_LINE_CHAR
        

for col in range(len(galaxy_map[0])):
    is_double = True
    for line in range(len(galaxy_map)):
        if galaxy_map[line][col] == "#":
            is_double = False
            break
    if is_double:
        for line in range(len(galaxy_map)):
            if galaxy_map[line][col] == ".":
                galaxy_map[line][col] = DOUBLE_COL_CHAR
            elif galaxy_map[line][col] == DOUBLE_LINE_CHAR:
                galaxy_map[line][col] = DOUBLE_INTERSECTION_CHAR


galaxy_list: list[tuple] = findGalaxyPositions(galaxy_map, "#")

all_galaxy_pairs = list(combinations(galaxy_list, 2))

print(f"{len(all_galaxy_pairs)} galaxy pairs")

step_count = 0
for (g1, g2) in all_galaxy_pairs:
    # moving in lines first:
    for i in range(g1[0], g2[0], 1 if g1[0] < g2[0] else -1): 
        step_count += 1
        if galaxy_map[i][g1[1]] in [DOUBLE_LINE_CHAR, DOUBLE_INTERSECTION_CHAR]:
            step_count += LINE_ADDITIONAL_WEIGHT

    #moving in columns then
    for j in range(g1[1], g2[1], 1 if g1[1] < g2[1] else -1): 
        step_count += 1
        if galaxy_map[g2[0]][j] in [DOUBLE_COL_CHAR, DOUBLE_INTERSECTION_CHAR]:
            step_count += COL_ADDITIONAL_WEIGHT

print(f"total step between galaxies: {step_count}")
