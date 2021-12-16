from ..functions import run_solution

input_filename = "./inputs/201701.txt"
expected_output = 1024


def solution(input_lines):

    sum = 0

    target_digit_distance = 0
    target_digit_location = 0

    position_on_line = 0

    clean_line = input_lines[0].strip()

    target_digit_distance = int(len(clean_line) / 2)

    for character in clean_line:
        position_on_line += 1

        if position_on_line + target_digit_distance >= len(clean_line):
            target_digit_location = (
                (position_on_line + target_digit_distance) - len(clean_line) - 1
            )
        else:
            target_digit_location = position_on_line + target_digit_distance - 1

        if character == clean_line[target_digit_location]:
            sum += int(character)

    print(sum)
    return sum


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
