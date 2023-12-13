import math


def find_row_mirror(pattern: list[str]): 
    for i, line in enumerate(pattern):
        for j in range(len(pattern)-1, i, -1):
            if line == pattern[j] and i != j and validate_mirror(pattern, i, j):
                return (i, j)
    return (-1, -1)


def validate_mirror(pattern: list[str], start: int, end: int) -> bool:
    for i in range(start, math.floor((end-start)/2)): 
        if pattern[start+i] != pattern[end-i]:
            return False
    
    return True


def find_col_mirror(pattern:list[str]):
    exploded_pattern = [ list(line) for line in pattern]
    reversed_exploded_pattern: list[tuple[str]] = list(map(list,zip(*exploded_pattern)))
    reversed_pattern =  [ "".join(line) for line in reversed_exploded_pattern]
    
    return find_row_mirror(reversed_pattern) 

def pretty_print_list(pList: list):
    for elem in pList:
        print(elem)


def get_top_part_to_count(input: tuple[int, int]) -> int: 
    return input[0] + math.floor((input[1]-input[0])/2) +1