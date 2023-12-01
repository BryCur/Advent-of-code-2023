
DIGITS_WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def exctractDigits(input: str) -> list[int]:
    lower_input = input.lower()
    sequence: list[int] = []

    for i, char in enumerate(lower_input):
        if char.isnumeric():
            sequence.append(int(char))
        else:
            for word in DIGITS_WORDS:
                if lower_input[i:i+len(word)] == word:
                    sequence.append(DIGITS_WORDS.index(word) +1)
                    break
                
    return sequence

def getValueFromSequence(seq: list[int]): 
    return seq[0] * 10 + seq[-1]

    