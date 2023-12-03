

def findNextSupportedSymbolInMatrix(matrix: list[str], startX: int, startY: int) -> (int, int):
    for x in range(startX, len(matrix)):
        for y in range(startY if startX == x else 0, len(matrix[x])): 
            if isCharSupportedSymbole(matrix[x][y]) :
                return (x, y)
    
    return (-1,-1)
            
def isCharSupportedSymbole(char: str):
    return not char.isalnum() and not char.isspace() and char != '.'


def getAdjacentNumberPositionsFrom(matrix: list[str], centerX: int, centerY: int) -> list[(int, int)]: 
    positions: list[(int,int)] = []

    startPosX = max(0, centerX-1)
    startPosY = max(0, centerY-1)

    stopPosX = min(len(matrix), centerX+2) # range does not include the stopIndex
    for x in range(startPosX, stopPosX): 
        stopPosY = min(len(matrix[x]), centerY+2)
        for y in range(startPosY, stopPosY): 
            if matrix[x][y].isdigit():
                positions.append((x,y))

    return positions

def consumeAndReturnNumberAtPosition(matrix: list[str], postStartX: int, posStartY: int) -> int:

    line: str = matrix[postStartX]

    numberStartIndex, numberStopIndex = getNumberStartAndEndPosOnLine(line, posStartY)

    number = int(line[numberStartIndex:numberStopIndex])
    matrix[postStartX] = eraseNumberAtPostion(line, numberStartIndex, numberStopIndex)
    return number

def getNumberStartAndEndPosOnLine(line: str, posStartY: int) -> (int, int):
    numberStartIndex = posStartY
    while numberStartIndex > 0 and line[numberStartIndex-1].isdigit():
        numberStartIndex -= 1

    numberStopIndex = posStartY
    while numberStopIndex < len(line) and line[numberStopIndex].isdigit():
        numberStopIndex += 1

    return (numberStartIndex, numberStopIndex)

def eraseNumberAtPostion(line: str, fromIndex: int, toIndex: int):
    new_line = line[:fromIndex] + ("0" * (toIndex -fromIndex)) + line[toIndex:]
    return new_line

def countAllUniqueNumberAroundPos(matrix: list[str], centerX: int, centerY: int): 
    digitPos = getAdjacentNumberPositionsFrom(matrix, centerX, centerY)
    setNumberPos: set = set()

    for (posX, posY) in digitPos:
        start, end = getNumberStartAndEndPosOnLine(matrix[posX], posY)
        setNumberPos.add(((posX,start), (posX, end)))
    
    return len(setNumberPos)