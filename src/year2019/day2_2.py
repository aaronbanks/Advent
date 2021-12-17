from ..functions import run_solution
import copy

input_filename = "./inputs/201902.txt"
expected_output = 8444


def solution(input_lines):

    initial_memory_state = list(map(int, input_lines[0].split(",")))

    noun = 0
    verb = 0

    required_output = 19690720

    solved = False
    answer = 0

    possible_input_values = range(0, 100)

    for possible_noun in possible_input_values:

        for possible_verb in possible_input_values:

            intcode = copy.copy(initial_memory_state)

            intcode[1] = possible_noun
            intcode[2] = possible_verb

            location_counter = 0

            while True:

                opcode = intcode[location_counter]

                perameter_pointer_1 = intcode[location_counter + 1]
                perameter_pointer_2 = intcode[location_counter + 2]
                perameter_pointer_3 = intcode[location_counter + 3]

                if opcode == 1:
                    intcode[perameter_pointer_3] = (
                        intcode[perameter_pointer_1] + intcode[perameter_pointer_2]
                    )

                elif opcode == 2:
                    intcode[perameter_pointer_3] = (
                        intcode[perameter_pointer_1] * intcode[perameter_pointer_2]
                    )

                elif opcode == 99:
                    break

                else:
                    print("opcode alingment error")

                location_counter += 4

            if intcode[0] == required_output:
                noun = possible_noun
                verb = possible_verb
                solved == True
                break

        if solved == True:
            break

    answer = 100 * noun + verb
    print(answer)
    return answer


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
