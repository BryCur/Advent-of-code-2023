import copy
from utils import *

matrix : list[list[str]] = []
target_step: int = 64
starting_pos: tuple
with open("day-21/input.txt") as file: 
    firstLineLength: int = -1
    for i, line in enumerate(file.readlines()):
        if "S" in line:
            starting_pos = (i, line.find("S"))
            line = line.replace("S", ".")

        matrix.append(list(line.strip()))
        if firstLineLength == -1:
            firstLineLength = len(matrix[-1])
        else:
            assert(firstLineLength == len(matrix[-1]))

pretty_print_list(matrix)
print(starting_pos)

count_reachable_plot = countReachablePlot(matrix, starting_pos, target_step)


pretty_print_list(matrix)
print(f"part 1 - total reachable plot after target step {count_reachable_plot}")





