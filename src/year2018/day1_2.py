from ..functions import run_solution

input_filename = "./inputs/201801.txt"
expected_output = 69074


def solution(input_lines):

    frequency = 0
    set_of_frequencies = {0}
    first_double = 0

    while True:
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

            if frequency in set_of_frequencies:
                first_double = frequency
                break

            set_of_frequencies.add(frequency)

        if first_double == frequency:
            break

    print(first_double)
    return first_double


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
