from utils import *

pipe_map: list[str]
starting_position: tuple

with open("day-10/example.txt", 'r') as f:
    pipe_map = list(map(str.strip,f.readlines()))
    
starting_position = findStartingPos(pipe_map, "S")

print(starting_position)