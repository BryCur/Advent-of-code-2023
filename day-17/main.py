from utils import *

matrix : list[list[int]] = []

with open("day-17/example.txt") as file: 
    for line in file:
        matrix.append(list(map(int, list(line.strip()))))


pretty_print_list(matrix)

start_pos = (0,0)
final_pos = (len(matrix)-1, len(matrix[1]-1))

