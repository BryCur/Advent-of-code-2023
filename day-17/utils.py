from enum import Enum
import copy

class Direction(Enum): 
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3


def pretty_print_list(pList: list[str]):
    for elem in pList:
        print(elem)
    print("-" * 50)
