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


class Arrival:
    arrivalNode: str
    totalStepRequired: int
    relativeStepRequired: int
    positionInSequence: int

    def __init__(self, node: str, total_step: int, previous_arrival_steps: int, sequence_position: int) -> None:
        self.arrivalNode= node
        self.totalStepRequired = total_step
        self.relativeStepRequired = total_step - previous_arrival_steps
        self.positionInSequence = sequence_position
        pass

    def __str__(self):
        return f"\nArrival(node: {self.arrivalNode}, totalstep: {self.totalStepRequired}, step from previous: {self.relativeStepRequired}, position in sequence: {self.positionInSequence})"
    def __repr__(self):
        return self.__str__()