from io import StringIO
from ..functions import run_solution

input_filename = "./inputs/201701.txt"
expected_output = 1164


def solution(input_lines):
    fake_input_file = StringIO("\n".join(input_lines))

    sum_of_digits = 0

    location_on_line = 0

    first_character_on_line = ""

    input_line = fake_input_file.readlines()
    fake_input_file.seek(0)

    for character in input_line[0]:

        current_digits = fake_input_file.readline(2)

        location_on_line += 1

        fake_input_file.seek(location_on_line)

        if location_on_line == 1:
            first_character_on_line = character

        if location_on_line == len(input_line[0]) - 1:
            if character == first_character_on_line:
                sum_of_digits += int(first_character_on_line)
            break

        if current_digits[0] == current_digits[1]:
            sum_of_digits += int(current_digits[0])

    print(sum_of_digits)
    return sum_of_digits


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
