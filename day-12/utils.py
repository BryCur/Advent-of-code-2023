
def process_line(line: str) -> tuple: 
    sequence, numbers = line.strip().split()
    numbers = list(map(int, numbers.split(",")))
    return (sequence, numbers)

