def HASH_algorithm_for_string(string: str) -> int:
    current_val = 0
    for char in string:
        current_val = HASH_algorithm_for_char(char, current_val)

    return current_val


def HASH_algorithm_for_char(char: str, current_value: int) -> int:
    current_value += ord(char)
    current_value *= 17
    return current_value % 256


def find_lens_index(box: list[tuple[str, int]], label: str):
    for i, lense in enumerate(box):
        if lense[0] == label:
            return i
        
    return None