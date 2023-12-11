from utils import *

pipe_map: list[list[str]] = []
starting_position: tuple


with open("day-10/input.txt", 'r') as f:
    for line in f.readlines():
        pipe_map.append([*line.strip()])
    
starting_position = findStartingPos(pipe_map, "S")

print(starting_position)

possible_starting_pipes = getStartingPipePossibleShape(pipe_map, starting_position)
print(f"possible shapes for start: {possible_starting_pipes}")
loopPath: list = []

pipe_map_copy: list[str] = pipe_map.copy()
for shape in possible_starting_pipes: 
    pipe_map_copy[starting_position[0]][starting_position[1]] = shape

    result = iterative_getPath(pipe_map_copy, starting_position)
    if result is not None and len(result) > len(loopPath):
        loopPath = result
        break

print(f"farthest tile: {int(len(loopPath) / 2)}")

print("flood fill")
# flood fill from borders
for i in range(len(pipe_map_copy)):
    if (i, 0) not in loopPath:
        pipe_map_copy[i][0] = "X"
    if (i, len(loopPath[i]) -1) not in loopPath:
        pipe_map_copy[i][-1] = "X"

# flood fill from borders
for i in range(len(pipe_map_copy[0])):
    if (0, i) not in loopPath:
        pipe_map_copy[0][i] = "X"
    if ( len(loopPath) -1, i) not in loopPath:
        pipe_map_copy[-1][0] = "X"

print("completing the flood")
maxi = len(pipe_map_copy)-1
for i in range(len(pipe_map_copy)):
    maxj = len(pipe_map_copy[i])-1
    for j in range(len(pipe_map_copy[i])):
        tile = pipe_map_copy[i][j]

        if (i,j) not in loopPath and hasAdjacentTileFlooded(pipe_map_copy, (i,j), "X"):
            pipe_map_copy[i][j] = "X"
        
        tile = pipe_map_copy[maxi-i][j]
        if (maxi-i,j) not in loopPath and hasAdjacentTileFlooded(pipe_map_copy, (maxi-i,j), "X"):
            pipe_map_copy[maxi-i][j] = "X"

print("counting unflooded tiles")
tileCount = 0
for i in range(len(pipe_map_copy)):
    for j in range(len(pipe_map_copy[i])):
        if (i,j) not in loopPath and pipe_map_copy[i][j] != "X":
            tileCount += 1

print(tileCount)
