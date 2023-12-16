from enum import Enum

class Direction(Enum): 
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


def pretty_print_list(pList: list[str]):
    for elem in pList:
        print(elem)
    print("-" * 50)


def beamShouldContinue(current_char: str, dir: Direction): 
    return current_char in ['.', '/', '\\'] or (current_char == '-' and dir in [Direction.LEFT, Direction.RIGHT]) or (current_char == '|' and dir in [Direction.UP, Direction.DOWN])

def get_next_direction(current_char: str, dir: Direction) -> Direction: 
    if current_char == '.':
        return dir

    if (dir == Direction.RIGHT and current_char == "/") or (dir == Direction.LEFT and current_char == "\\"):
        return Direction.UP
    elif (dir == Direction.LEFT and current_char == "/") or (dir == Direction.RIGHT and current_char == "\\"):
        return Direction.DOWN
    elif (dir == Direction.UP and current_char == "/") or (dir == Direction.DOWN and current_char == "\\"):
        return Direction.RIGHT
    elif (dir == Direction.DOWN and current_char == "/") or (dir == Direction.UP and current_char == "\\"):
        return Direction.LEFT
    
    return dir

def getNewBeams(matrix: list, posX: int, posY: int, dir: Direction) -> list:
    current_char = matrix[posX][posY]
    if current_char not in ['-', '|']:
        return []

    to_process = []
    if dir in [Direction.DOWN, Direction.UP] and current_char == '-':
        if posY > 0:
            to_process.append(((posX, posY-1), Direction.LEFT))
        if posY < len(matrix[posX])-1:
            to_process.append(((posX, posY+1), Direction.RIGHT))

    elif dir in [Direction.LEFT, Direction.RIGHT] and current_char == '|':
        if posX > 0:
            to_process.append(((posX-1, posY), Direction.UP))
        if posX < len(matrix)-1:
            to_process.append(((posX+1, posY), Direction.DOWN))

    return to_process

def beam_matrix_from_starting_tile_and_direction(matrix: list, beamed_matrix: list, starting_beam: tuple[tuple[int, int], Direction]) -> int:
    beamed_matrix_copy = beamed_matrix.copy()
    processed_beams : list[tuple[tuple[int, int], Direction]] = []
    beams_to_process : list[tuple[tuple[int, int], Direction]] = [starting_beam]

    while len(beams_to_process) > 0:

        current_beam = beams_to_process.pop(0)

        if current_beam in processed_beams:
            continue
        else: 
            processed_beams.append(current_beam)

        posX, posY = current_beam[0]
        direction: Direction = current_beam[1]
        beamed_matrix_copy[posX][posY] += 1

        while beamShouldContinue(matrix[posX][posY], direction):
            direction = get_next_direction(matrix[posX][posY], direction)
            if direction == Direction.RIGHT:
                if posY +1 < len(matrix[posX]):
                    posY += 1
                else: 
                    break
            elif direction == Direction.LEFT:
                if posY > 0:
                    posY -= 1
                else: 
                    break
            elif direction == Direction.DOWN:
                if posX +1 < len(matrix):
                    posX += 1
                else: 
                    break
            elif direction == Direction.UP:
                if posX > 0:
                    posX -= 1
                else: 
                    break

            beamed_matrix_copy[posX][posY] += 1
        
        
        # beam is stopping, need to start a new one
        beams_to_process += getNewBeams(matrix, posX, posY, direction)
    
    return count_beamed_tiles(beamed_matrix_copy)

def count_beamed_tiles(beamed_matrix: list[list[int]]): 
    total_beamed_tiles: int = 0
    for line in beamed_matrix:
        for tile in line:
            if tile > 0:
                total_beamed_tiles += 1

    return total_beamed_tiles
