
from enum import Enum
class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3

pipes_connecting_north: set = set(['L', 'J', '|'])
pipes_connecting_south: set = set(['7', 'F', '|'])
pipes_connecting_east: set = set(['-', 'L', 'F'])
pipes_connecting_west: set = set(['-', '7', 'J'])


def findStartingPos(matrix: list[list[str]], startChar: str) -> tuple: 
     for i, line in enumerate(matrix):
        if startChar in line:
            return (i, line.index(startChar))

def recursive_getPath(matrix: list[list[str]], position: tuple, previous_steps: list = []) -> list :
    (currX, currY) = position
    curPipe = matrix[currX][currY]

    if curPipe in pipes_connecting_north and currX > 0 and matrix[currX-1][currY] in pipes_connecting_south:
        # the pipe on the north is connected to the current pipe
        if len(previous_steps) >= 3 and (currX-1, currY) == previous_steps[0]: # loop is found! return
            return [position]
        elif (currX-1,currY) not in previous_steps:
            result_next_step = getNextSteps(matrix, (currX-1, currY), previous_steps + [position])
            if result_next_step != None:
                return [position] + result_next_step
    
    if curPipe in pipes_connecting_east and currY < len(matrix[currX])-1 and matrix[currX][currY+1] in pipes_connecting_west:
        # the pipe on the north is connected to the current pipe
        if len(previous_steps) >= 3 and (currX, currY+1) == previous_steps[0]: # loop is found! return
            return [position]
        elif (currX,currY+1) not in previous_steps:
            result_next_step = getNextSteps(matrix, (currX, currY +1), previous_steps + [position])
            if result_next_step != None:
                return [position] + result_next_step
            
    if curPipe in pipes_connecting_south and currX < len(matrix)-1 and matrix[currX+1][currY] in pipes_connecting_north:
        # the pipe on the north is connected to the current pipe
        if len(previous_steps) >= 3 and (currX+1, currY) == previous_steps[0]: # loop is found! return
            return [position]
        elif (currX+1,currY) not in previous_steps:
            result_next_step = getNextSteps(matrix, (currX+1, currY), previous_steps + [position])
            if result_next_step != None:
                return [position] + result_next_step
            
    if curPipe in pipes_connecting_west and currY > 0 and matrix[currX][currY-1] in pipes_connecting_east:
        # the pipe on the north is connected to the current pipe
        if len(previous_steps) >= 3 and (currX, currY-1) == previous_steps[0]: # loop is found! return
            return [position]
        elif (currX,currY-1) not in previous_steps:
            result_next_step = getNextSteps(matrix, (currX, currY -1), previous_steps + [position])
            if result_next_step != None:
                return [position] + result_next_step


    return None

def getStartingPipePossibleShape(matrix: list[int], position: tuple) -> set:
    (posX, posY) = position
    possible_shapes: set = set()

    northPipe = matrix[posX -1][posY]
    southPipe = matrix[posX +1][posY]
    westPipe = matrix[posX][posY-1]
    eastPipe = matrix[posX][posY+1]

    if northPipe in pipes_connecting_south:
        if westPipe in pipes_connecting_east:
            possible_shapes = possible_shapes.union(pipes_connecting_north.intersection(pipes_connecting_west))
        if eastPipe in pipes_connecting_west:
            possible_shapes = possible_shapes.union(pipes_connecting_north.intersection(pipes_connecting_east))
        if southPipe in pipes_connecting_north:
            possible_shapes = possible_shapes.union(pipes_connecting_north.intersection(pipes_connecting_south))
    
    if southPipe in pipes_connecting_north:
        if westPipe in pipes_connecting_east:
            possible_shapes = possible_shapes.union(pipes_connecting_south.intersection(pipes_connecting_west))
        if eastPipe in pipes_connecting_west:
            possible_shapes = possible_shapes.union(pipes_connecting_south.intersection(pipes_connecting_east))
        if northPipe in pipes_connecting_south: # already checked
            possible_shapes = possible_shapes.union(pipes_connecting_south.intersection(pipes_connecting_north))
        
    if eastPipe in pipes_connecting_west:
        if westPipe in pipes_connecting_east:
            possible_shapes = possible_shapes.union(pipes_connecting_east.intersection(pipes_connecting_west))
        if northPipe in pipes_connecting_south:
            possible_shapes = possible_shapes.union(pipes_connecting_east.intersection(pipes_connecting_north))
        if southPipe in pipes_connecting_north:
            possible_shapes = possible_shapes.union(pipes_connecting_east.intersection(pipes_connecting_south))
        
    if westPipe in pipes_connecting_east:
        if eastPipe in pipes_connecting_west:
            possible_shapes = possible_shapes.union(pipes_connecting_west.intersection(pipes_connecting_east))
        if southPipe in pipes_connecting_north:
            possible_shapes = possible_shapes.union(pipes_connecting_west.intersection(pipes_connecting_south))
        if northPipe in pipes_connecting_south:
            possible_shapes = possible_shapes.union(pipes_connecting_west.intersection(pipes_connecting_north))
        

    return possible_shapes



def iterative_getPath (matrix: list[list[str]], starting_pos: tuple) -> list :
    current_position = starting_pos
    coming_from: Direction = None
    path: list[tuple] = []
    
    while True:
        path.append(current_position)
        (currX, currY) = current_position
        curPipe = matrix[currX][currY]

        canMoveNorth = curPipe in pipes_connecting_north and currX > 0 and coming_from != Direction.NORTH
        if canMoveNorth and matrix[currX-1][currY] in pipes_connecting_south :
            # the pipe on the north is connected to the current pipe
            
            next_pipe_pos = (currX-1, currY)
            if next_pipe_pos == starting_pos: # completed the loop
                return path
            else: # move to north, will be comming from south
                current_position = next_pipe_pos
                coming_from = Direction.SOUTH
                continue

        canMoveEast = curPipe in pipes_connecting_east and currY < len(matrix[currX])-1 and coming_from != Direction.EAST
        if canMoveEast and matrix[currX][currY+1] in pipes_connecting_west :
            # the pipe on the east is connected to the current pipe
            
            next_pipe_pos = (currX, currY+1)
            if next_pipe_pos == starting_pos: # completed the loop
                return path
            else: # move to east, will be comming from west
                current_position = next_pipe_pos
                coming_from = Direction.WEST
                continue
        
        canMoveSouth = curPipe in pipes_connecting_south and currX < len(matrix)-1 and coming_from != Direction.SOUTH
        if canMoveSouth and matrix[currX+1][currY] in pipes_connecting_north:
            next_pipe_pos = (currX+1, currY)
            if next_pipe_pos == starting_pos: # completed the loop
                return path
            else: # move to south, will be comming from north
                current_position = next_pipe_pos
                coming_from = Direction.NORTH
                continue

        canMoveWest = curPipe in pipes_connecting_west and currY > 0 and coming_from != Direction.WEST
        if canMoveWest and matrix[currX][currY-1] in pipes_connecting_east:
            next_pipe_pos = (currX, currY-1)
            if next_pipe_pos == starting_pos: # completed the loop
                return path
            else: # move to west, will be comming from east
                current_position = next_pipe_pos
                coming_from = Direction.EAST
                continue

        # if we reach this point, then the path leads to a dead end
        return None

    return None

def hasAdjacentTileFlooded(matrix: list[list], position: tuple, floodedChar: str):
    (posX, posY) = position

    minX = max(0, posX-1)
    maxX = min(len(matrix), posX+2)
    minY = max(0, posY-1)
    maxY = min(len(matrix[posX]), posY+2)

    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if matrix[x][y] == floodedChar:
                return True
    return False
