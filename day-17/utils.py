from enum import Enum
import copy

class Direction(Enum): 
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

class Node: 
    position: tuple
    neighbours: dict[Direction, 'Node']
    visited: bool = False
    heatLoss: int = 0

    def __init__(self, position: tuple, value: int, nLeft = None, nRight = None, nUp = None, nDown = None) -> None:

        self.position = position

        self.neighbours = dict()
        self.neighbours[Direction.LEFT] = nLeft
        self.neighbours[Direction.RIGHT] = nRight
        self.neighbours[Direction.UP] = nUp
        self.neighbours[Direction.DOWN] = nDown

        self.visited = False
        self.heatLoss = value

    def setVisited(self, newval: bool) -> None:
        self.visited = newval

    def getNeighbourAtDirection(self, direction: Direction): 
        return self.neighbours[direction]
    
    def isVisited(self) -> bool: 
        return self.visited
    
    def addNeighbour(self, direction: Direction, value): 
        self.neighbours[direction] = value



def pretty_print_list(pList: list[str]):
    for elem in pList:
        print(elem)
    print("-" * 50)


def findPathToDestination(destination: tuple[int, int], currentNode: Node, minheatLoss: int, currentPath: list, currentHeatLoss: int, lastDirection: Direction, sameDirectionCount: int):
    if currentNode.position == destination:
        # print(f"destination reached, minHeatloss: {minheatLoss}, current heatloss: {currentHeatLoss}, path: {currentPath}")
        if minheatLoss == -1 or minheatLoss > currentHeatLoss:
            minheatLoss = currentHeatLoss
        return minheatLoss
    
    
    currentNode.setVisited(True)
    currentPath.append(currentNode.position)


    for key, val in currentNode.neighbours.items():
        if val is not None and not val.isVisited() and (key != lastDirection or sameDirectionCount < 3):
            minheatLoss = findPathToDestination(destination, val, minheatLoss, currentPath, (currentHeatLoss + val.heatLoss), key, sameDirectionCount +1 if key == lastDirection else 0)

    currentNode.setVisited(False)
    currentPath.pop()

    return minheatLoss