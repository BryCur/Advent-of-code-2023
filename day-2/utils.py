MAX_VALUES = {
    "blue": 14,
    "green": 13,
    "red": 12
}

def getGameId(line: str) -> int :
    split_id_data = line.split(":")
    str_game_id = split_id_data[0].split(" ")[-1]
    return int(str_game_id) if str_game_id.isdigit() else 0

def getSequence(line: str) -> list: 
    split_id_data = line.split(":")
    return split_id_data[-1].split(";")

def isSequencePossible(sequence: list[str]) -> bool:
    for draft in sequence:
        drafted_dice = draft.split(",")
        for die in drafted_dice: 
            [count, colour] = die.strip().split(" ")
            if count.isdigit() and colour in MAX_VALUES.keys() and int(count) > MAX_VALUES[colour]:
                return False
    
    return True


