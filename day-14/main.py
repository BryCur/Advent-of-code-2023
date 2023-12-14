from utils import *
import itertools

stone_map: list[str] = []
target_cycle = 1000000000
with open("day-14/input.txt") as file:
    stone_map = list(map(str.strip, file.readlines()))


current_load = None
load_history = []
map_history = []
current_map = stone_map.copy()
while True:


    current_map = tilt_map_north(current_map)
    current_map = tilt_map_west(current_map)
    current_map = tilt_map_south(current_map)
    current_map = tilt_map_east(current_map)

    current_load = compute_map_load(current_map)
    load_history.append(current_load)

    if current_map in map_history:
        break

    map_history.append(current_map)


start_of_loop = map_history.index(current_map)
loop = load_history[start_of_loop:]
loop_length = len(map_history[start_of_loop:])
cycle_before_loop = len(map_history[:start_of_loop])

print(f"loop of {len(load_history)} cycle found; position of loop start in history: {map_history.index(current_map)} ")

something = (target_cycle - cycle_before_loop) % loop_length
print(f"part 2 - solution after target cycle: {loop[something-1]}")




