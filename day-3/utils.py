

def findNextSupportedSymbolInMatrix(matrix: list[str], startX: int, startY: int) -> (int, int):
    for x in range(startX, len(matrix)):
        for y in range(startY, len(matrix[x])): 
            if isCharSupportedSymbole(matrix[x][y]) :
                return (x, y)
    
    return (-1,-1)
            
def isCharSupportedSymbole(char: str):
    return not char.isalnum() and char != '.'


def getAdjacentNumberPositionsFrom(matrix: list[str], centerX: int, centerY: int) -> list[(int, int)]: 
    positions: list[(int,int)] = []

    startPosX = max(0, centerX-1)
    startPosY = max(0, centerY-1)

    stopPosX = min(len(matrix), centerX+1)
    for x in range(startPosX, stopPosX+1): # range does not include the stopIndex
        stopPosY = min(len(matrix[x]), centerY+1)
        for y in range(startPosY, stopPosY+1): 
            currChar = matrix[x][y]
            if matrix[x][y].isdigit():
                positions.append((x,y))

    return positions

def consumeNumberAtPosition(matrix: list[str], postStartX: int, posStartY: int) -> int:

    line: str = matrix[postStartX]

    numberStartIndex = posStartY
    while numberStartIndex > 0 and line[numberStartIndex-1].isdigit():
        numberStartIndex -= 1

    numberStopIndex = posStartY
    while numberStopIndex < len(line) and line[numberStopIndex].isdigit():
        numberStopIndex += 1

    number = int(line[numberStartIndex:numberStopIndex])
    new_line = line[:numberStartIndex] + ("0" * (numberStopIndex -numberStartIndex)) + line[numberStopIndex:]
    matrix[postStartX] = new_line
    return number