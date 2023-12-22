from utils import *

matrix : list[list[int]] = []

with open("day-17/example.txt") as file: 
    firstLineLength: int = -1
    for line in file.readlines():
        matrix.append(list(map(int, list(line.strip()))))
        if firstLineLength == -1:
            firstLineLength = len(matrix[-1])
        else:
            assert(firstLineLength == len(matrix[-1]))


pretty_print_list(matrix)

node_dict : dict[tuple, Node] = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        currNode = Node((i,j), matrix[i][j])
        if (i-1, j) in node_dict:
            currNode.addNeighbour(Direction.UP, node_dict[(i-1, j)])
            node_dict[(i-1, j)].addNeighbour(Direction.DOWN, currNode)
        if (i+1, j) in node_dict:
            currNode.addNeighbour(Direction.DOWN, node_dict[(i+1, j)])
            node_dict[(i+1, j)].addNeighbour(Direction.UP, currNode)
        if (i, j-1) in node_dict:
            currNode.addNeighbour(Direction.LEFT, node_dict[(i, j-1)])
            node_dict[(i, j-1)].addNeighbour(Direction.RIGHT, currNode)
        if (i, j+1) in node_dict:
            currNode.addNeighbour(Direction.RIGHT, node_dict[(i, j+1)])
            node_dict[(i, j+1)].addNeighbour(Direction.LEFT, currNode)

        node_dict[(i,j)] = currNode
        

start_pos = (0,0)
final_pos = (len(matrix)-1, len(matrix[1])-1)


starting_node = node_dict[start_pos]
destination  = node_dict[final_pos]

minHeatlossPath: list[tuple[int, int]] = None
minHeatloss = -1

minHeatloss = findPathToDestination(destination.position, starting_node, minHeatloss, [], 0, None, 0)

print(f"testing a little; heatloss: {minHeatloss}, path {minHeatlossPath}")


