from .. import viz
from ..functions import run_solution

input_filename = "./inputs/201503.txt"
expected_output = 2081


def solution(input_lines):
    set_of_houses = {(0, 0)}

    total_number_of_houses = 1

    horizontal_position = 0
    vertical_position = 0

    for line in input_lines:
        current_line_contents = line.strip()

        for character in current_line_contents:
            if character == "^":
                vertical_position += 1

            if character == "v":
                vertical_position -= 1

            if character == ">":
                horizontal_position += 1

            if character == "<":
                horizontal_position -= 1

            current_position = (horizontal_position, vertical_position)

            if current_position in set_of_houses:
                pass
            else:
                set_of_houses.add(current_position)
                total_number_of_houses += 1

            viz.line_to(horizontal_position, vertical_position)

    print(f"The total number of houses visited is: {total_number_of_houses}")
    return total_number_of_houses


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
