def pretty_print_list(pList: list[str]):
    for elem in pList:
        print(elem)
    print("-" * 50)

def reverse_string_list(pList: list[str]):
    exploded_list = [ list(line) for line in pList]
    reversed_exploded_list: list[tuple[str]] = list(map(list,zip(*exploded_list)))
    return [ "".join(line) for line in reversed_exploded_list]

def shift_stones_in_line(map_line: str, to_left = True) -> str:
    splitted_by_stop_stone = map_line.split("#")
    sorted_exploded_split = list(map(lambda x: sorted(x, reverse=to_left), splitted_by_stop_stone))
    sorted_split = list(map("".join, sorted_exploded_split))
    return "#".join(sorted_split)



def tilt_map_west(map: list[str]) -> list[str]:
    updated_map = []
    for line in map: 
        updated_map.append(shift_stones_in_line(line))
    return updated_map

def tilt_map_east(map: list[str]) -> list[str]:
    updated_map = []
    for line in map: 
        updated_map.append(shift_stones_in_line(line, False))
    return updated_map

def tilt_map_north(map: list[str]) -> list[str]:
    reversed_map = reverse_string_list(map)
    updated_map = []
    for line in reversed_map: 
        updated_map.append(shift_stones_in_line(line))
    return reverse_string_list(updated_map)

def tilt_map_south(map: list[str]) -> list[str]:
    reversed_map = reverse_string_list(map)
    updated_map = []
    for line in reversed_map: 
        updated_map.append(shift_stones_in_line(line, False))
    return reverse_string_list(updated_map)

def compute_map_load(map: list[str]): 
    total_load = 0
    for i, line in enumerate(map):
        total_load += (len(map) -i)  * line.count("O")
    return total_load