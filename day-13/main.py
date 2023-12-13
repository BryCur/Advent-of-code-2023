from utils import *
import itertools

list_of_pattern: list[list[str]] = []
with open("day-13/input.txt") as file:
    current_pattern: list[str] = []
    for line in file.readlines(): 
        if line.isspace():
            list_of_pattern.append(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(line.strip())
    list_of_pattern.append(current_pattern)


count= 0
found_in_row = False
for pattern in list_of_pattern:
    mirror_range_row = find_row_mirror(pattern)
    mirror_range_col = find_col_mirror(pattern)

    if (mirror_range_row[1] - mirror_range_row[0]) < (mirror_range_col[1] - mirror_range_col[0]):
        count += get_top_part_to_count(mirror_range_col) 
    else: 
        count += get_top_part_to_count(mirror_range_row)* 100

print(count)