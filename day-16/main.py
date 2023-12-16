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
print(f"part 1 - tiles beamed up: {total_beamed_tiles}")


# part 2
max_beamed_tile = 0

# starting from the side lines

for i in range(len(matrix)):
    coverage1 = beam_matrix_from_starting_tile_and_direction(matrix, beamed_matrix, ((i, 0), Direction.RIGHT))
    coverage2 = beam_matrix_from_starting_tile_and_direction(matrix, beamed_matrix, ((i, len(matrix[i])-1), Direction.LEFT))
    max_beamed_tile = max(max_beamed_tile, coverage1, coverage2)

for i in range(len(matrix[0])):
    coverage1 = beam_matrix_from_starting_tile_and_direction(matrix, beamed_matrix, ((0, i), Direction.DOWN))
    coverage2 = beam_matrix_from_starting_tile_and_direction(matrix, beamed_matrix, ((len(matrix)-1, i), Direction.UP))
    max_beamed_tile = max(max_beamed_tile, coverage1, coverage2)

print(f"part 2 - max beamed configuration: {max_beamed_tile}")