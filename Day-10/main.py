from utils import *

pipe_map: list[str]
starting_position: tuple


with open("day-10/input.txt", 'r') as f:
    pipe_map = list(map(str.strip,f.readlines()))
    
starting_position = findStartingPos(pipe_map, "S")

print(starting_position)

possible_starting_pipes = getStartingPipePossibleShape(pipe_map, starting_position)
print(f"possible shapes for start: {possible_starting_pipes}")
loopPath: list = []

pipe_map_copy: list[str] = pipe_map.copy()
for shape in possible_starting_pipes: 
    pipe_map_copy[starting_position[0]] = pipe_map[starting_position[0]].replace("S", shape)

    result = iterative_getPath(pipe_map_copy, starting_position)
    if result is not None and len(result) > len(loopPath):
        loopPath = result

print(f"loop path: {loopPath}")
print(f"farthest tile: {int(len(loopPath) / 2)}")