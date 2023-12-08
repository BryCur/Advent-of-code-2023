def process_input_tuple(input: str) -> tuple:
    return tuple(input.strip().replace("(", "").replace(")", "").split(", "))


def getNextStep(map: dict, key: str, direction: str) -> str:
    assert(key in map)
    return map.get(key)[1 if direction == "R" else 0]


def shouldContinue(nodes: list[str]) -> bool: 
    for node in nodes: 
        if node[-1] != 'Z': 
            return True
        
    return False