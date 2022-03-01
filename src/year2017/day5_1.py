from ..functions import run_solution

input_filename = "./inputs/201705.txt"
expected_output = 358309


def solution(input_lines):

    instruction_list = []

    for line in input_lines:
        instruction_list.append(int(line))

    steps_taken = 0
    currnt_position_in_list = 0

    while True:
        
        try:
            store_current_position = currnt_position_in_list
            currnt_position_in_list += instruction_list[currnt_position_in_list]

            instruction_list[store_current_position] += 1
            steps_taken += 1

        except IndexError:
            print(f"Steps taken to reach exit: {steps_taken}")
            break

    return steps_taken

if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
