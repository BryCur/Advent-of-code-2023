

firstDigit: int = -1
lastdigit: int = -1
totalValue: int = 0

numbersInLetters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt') as file: 
    lines: list[str] = file.readlines()
    for line in lines:
        firstDigit = -1
        lastdigit = -1

        # goes char by char in the line
        for i in range(len(line)):
            if line[i].isnumeric() and firstDigit == -1:
                firstDigit = int(line[i])
            if line[-(i+1)].isnumeric() and lastdigit == -1:
                lastdigit = int(line[-(i+1)])
            if lastdigit != -1 and firstDigit != -1:
                break

        totalValue += (firstDigit*10) + lastdigit

print(totalValue)