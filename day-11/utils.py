def pretty_print_map(map: list[list]): 
    for line in map:
        print("".join(line))

def findGalaxyPositions(matrix: list[str], galaxyChar: str) -> (int, int):
    positions: list = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])): 
            if matrix[x][y] == galaxyChar :
                positions.append((x, y))
    
    return positions