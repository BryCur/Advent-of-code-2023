
pipes_connecting_north: set = set(['L', 'J', '|'])
pipes_connecting_south: set = set(['7', 'F', '|'])
pipes_connecting_east: set = set(['-', 'L', 'F'])
pipes_connecting_west: set = set(['-', '7', 'J'])


def findStartingPos(matrix: list[str], startChar: str) -> tuple: 
     for i, line in enumerate(matrix):
        if startChar in line:
            return (i, line.index(startChar))

def getNextStep(matrix: list[str], position: tuple, previousPos: tuple | None) -> tuple :
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