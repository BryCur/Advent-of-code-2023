def getNextSequence(numbers: list[int]) -> list[int]:
    next_seq: list[int] = []
    for i in range(len(numbers) -1):
        next_seq.append(numbers[i+1] - numbers[i])
    
    return next_seq;


def getNextNumberInSequence(seq: list[int]):
    next_sequence = getNextSequence(seq)

    if len(set(next_sequence)) == 1: # sequence composed of only one number
        return seq[-1] + next_sequence[-1]
    else:
        return seq[-1] + getNextNumberInSequence(next_sequence)
    


def getPreviousNumberInSequence(seq: list[int]):
    next_sequence = getNextSequence(seq)

    if len(set(next_sequence)) == 1: # sequence composed of only one number
        return seq[0] - next_sequence[0]
    else:
        return seq[0] - getPreviousNumberInSequence(next_sequence)