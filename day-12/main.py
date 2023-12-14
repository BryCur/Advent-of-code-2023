from utils import *
import itertools

input: list[tuple[str, list[int]]] = []
with open("day-12/input.txt") as file:
    input = list(map(process_line, file.readlines()))

count = 0
for i, (defective, numbers) in enumerate(input):
    print(f"processing {i}/{len(input)} line")
    chars_to_add = get_char_to_add(defective, numbers)

    list_of_combination: list[tuple[str]] = list(set(itertools.permutations([*chars_to_add])))

    for combi in list_of_combination:
        defect_copy:str = defective
        
        filled_input = get_filled_string(defective, combi)

        if string_match_sequence(filled_input, numbers):
            count += 1

print(count)