from ..functions import run_solution

input_filename = "./inputs/201801.txt"
expected_output = 510


def solution(input_lines):

    frequency = 0

    for line in input_lines:

        if line[0] == "+":
            modifier_is_positive = True
        elif line[0] == "-":
            modifier_is_positive = False

        line_value = line[1:]

        if modifier_is_positive == True:
            frequency += int(line_value)
        if modifier_is_positive == False:
            frequency -= int(line_value)

    print(frequency)
    return frequency


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
