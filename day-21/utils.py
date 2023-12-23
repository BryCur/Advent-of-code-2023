def pretty_print_list(pList: list[str]):
    for elem in pList:
        print(elem)
    print("-" * 50)


def countReachablePlot(matrix: list[list[str]], starting_pos: tuple[int, int], target_step: int) -> int:
    reached_pos: list[tuple[int, int]] = []
    count = 0

    to_process: list[tuple[int, int]] = [starting_pos]

    for steps in range(target_step+1):
        to_process_next_step = []

        for (posX, posY) in to_process:
            if matrix[posX][posY] != ".":
                continue

            if (target_step-steps) % 2 == 0: 
                reached_pos.append((posX, posY))
                count += 1
                matrix[posX][posY] = "0" # mark as visited
            else: 
                matrix[posX][posY] = "/" # mark as visited
            
            if posX > 0 and matrix[posX-1][posY] == '.':
                to_process_next_step.append((posX-1, posY))
            
            if posX < len(matrix)-1 and matrix[posX+1][posY] == '.':
                to_process_next_step.append((posX+1, posY))

            if posY > 0 and matrix[posX][posY-1] == '.':
                to_process_next_step.append((posX, posY-1))

            if posY < len(matrix[posX])-1 and matrix[posX][posY+1] == '.':
                to_process_next_step.append((posX, posY+1))

        to_process = to_process_next_step

    return count


