from io import StringIO
from ..functions import run_solution

input_filename = "./inputs/201501.txt"
expected_output = 74


def solution(input_lines):
    fake_input_file = StringIO("\n".join(input_lines))

    floor = 0

    EOF = False

    while EOF == False:
        current_character = fake_input_file.read(1)

        if current_character == "(":
            floor += 1
        elif current_character == ")":
            floor -= 1
        elif current_character == "":
            EOF = True
        else:
            pass

    # Below is an alternate way to write this.
    # for line in fake_input_file:
    #     for character in line:
    #         if character == '(':
    #             floor += 1
    #         elif character == ')':
    #             floor -= 1
    #         else:
    #             pass

    print(f"The instructions take santa to floor: {floor}")

    return floor


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
