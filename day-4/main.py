from utils import *

PUZZLE_PART = 2
totalValue = 0
with open("day-4/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        winning = getWinningNumber(line)
        checking = getPlayingNumber(line)

        intersection = getListIntersection(winning, checking)
        print(intersection)
        if len(intersection) != 0:
            totalValue += pow(2, len(intersection) -1)




print(totalValue)