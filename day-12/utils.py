import functools


def process_line(line: str) -> tuple: 
    sequence, numbers = line.strip().split()
    numbers = list(map(int, numbers.split(",")))
    return (sequence, numbers)

def string_match_sequence(string: str, seq: list[int]) -> bool:
    splitted_str = [s for s in string.split(".") if s]
    length_sequence = list(map(len, splitted_str))
    return length_sequence == seq

def string_match_original(original:str, tried: str) -> bool:
    for i, char in enumerate(original):
          if char != "?" and char != tried[i]:
               return False
    return True


def get_char_to_add(defective: str, sequence: list[int]) -> str : 
    expected_number_of_spring = sum(sequence)
    current_number_of_spring = defective.count("#")
    count_of_question_marks = defective.count("?")

    springs_to_add = expected_number_of_spring - current_number_of_spring
    return "#"* springs_to_add + "."*(count_of_question_marks-springs_to_add)

def get_filled_string(defect: str, replacement: tuple): 
    replacement_list = list(replacement)

    result: str = defect
    while result.find("?") != -1:
            result = result.replace("?", replacement_list.pop(0), 1)

    return result

def get_defective_sequence(sequence: list[int]):
     return ["#" * num for num in sequence]

