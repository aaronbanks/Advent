from ..functions import run_solution

input_filename = "./inputs/201602.txt"
expected_output = "C1A88"


def solution(input_lines):

    keypad = (
        ("X", "X", "1", "X", "X"),
        ("X", "2", "3", "4", "X"),
        ("5", "6", "7", "8", "9"),
        ("X", "A", "B", "C", "X"),
        ("X", "X", "D", "X", "X"),
    )

    current_keypad_location = [2, 1]

    bathroom_code = []

    for line in input_lines:
        current_line_contents = line.strip()

        for character in current_line_contents:

            previous_keypad_location = list(current_keypad_location)

            if character == "L":
                if current_keypad_location[1] == 0:
                    pass
                else:
                    current_keypad_location[1] -= 1

            elif character == "R":
                if current_keypad_location[1] == 4:
                    pass
                else:
                    current_keypad_location[1] += 1

            elif character == "U":
                if current_keypad_location[0] == 0:
                    pass
                else:
                    current_keypad_location[0] -= 1

            elif character == "D":
                if current_keypad_location[0] == 4:
                    pass
                else:
                    current_keypad_location[0] += 1

            if keypad[current_keypad_location[0]][current_keypad_location[1]] == "X":
                current_keypad_location = previous_keypad_location

        print(current_keypad_location)
        bathroom_code.append(
            keypad[current_keypad_location[0]][current_keypad_location[1]]
        )

    bathroom_code = "".join(map(str, bathroom_code))
    print(f"The bathroom code is: {bathroom_code}")
    return bathroom_code


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
