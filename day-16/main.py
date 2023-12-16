from utils import *

matrix : list[list[str]] = []
beamed_matrix: list[list[int]] = []
with open("day-16/input.txt") as file: 
    for line in file:
        matrix.append(list(line.strip()))
        beamed_matrix.append( [0] * len(matrix[-1]))

#pretty_print_list(beamed_matrix)
#pretty_print_list(matrix)

# part 1
starting_beam : tuple[tuple[int, int], Direction] = ((0,0), Direction.RIGHT)
total_beamed_tiles: int = beam_matrix_from_starting_tile_and_direction(matrix, beamed_matrix, starting_beam)
print(f"tiles beamed up: {total_beamed_tiles}")
