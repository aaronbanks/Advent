from ..functions import run_solution

input_filename = "./inputs/202102.txt"
expected_output = 1857958050


def solution(input_lines):

    current_line_contents = []

    list_of_forward_directional_inputs = []

    current_line = 0
    aim = 0
    depth = 0

    for line in input_lines:

        current_line += 1

        current_line_contents = (line.strip()).split(" ", 1)

        print(f"Current line #: {current_line}")
        print(f"Current line contents: {current_line_contents}")

        if "forward" in current_line_contents[0]:
            list_of_forward_directional_inputs.append(int(current_line_contents[1]))
            depth += aim * int(current_line_contents[1])

        elif "up" in current_line_contents[0]:
            aim -= int(current_line_contents[1])

        elif "down" in current_line_contents[0]:
            aim += int(current_line_contents[1])

    final_horizontal_position = sum(list_of_forward_directional_inputs)
    answer = final_horizontal_position * depth

    print(f"The final horizontal position is: {final_horizontal_position}")
    print(f"The final depth is: {depth}")
    print(f"The answer to the problem is: {answer}")

    return answer


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
