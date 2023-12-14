from utils import *
import itertools

stone_map: list[str] = []
with open("day-14/input.txt") as file:
    stone_map = list(map(str.strip, file.readlines()))

#pretty_print_list(stone_map)
reversed_map = reverse_string_list(stone_map)
#pretty_print_list(reversed_map)

processed_reversed_map = []
for line in reversed_map:
    shifted_line = shift_stones_in_line(line)
    processed_reversed_map.append(shifted_line)

reversed_reversed_map = reverse_string_list(processed_reversed_map)

# pretty_print_list(reversed_reversed_map)

total_load = 0
for i, line in enumerate(reversed_reversed_map):
    total_load += (len(reversed_reversed_map) -i)  * line.count("O")

print(f"part 1 - total load: {total_load}")