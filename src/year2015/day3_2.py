from ..functions import run_solution

input_filename = "./inputs/201503.txt"
expected_output = 2341


def solution(input_lines):

    set_of_houses = {(0, 0)}

    total_number_of_houses = 1

    santa_horizontal_position = 0
    santa_vertical_position = 0

    robo_santa_horizontal_position = 0
    robo_santa_vertical_position = 0

    santa_toggle = True
    # santa_toggle = True means it's real santa's turn

    for line in input_lines:
        current_line_contents = line.strip()

        for character in current_line_contents:

            if character == "^":
                if santa_toggle == True:
                    santa_vertical_position += 1
                if santa_toggle == False:
                    robo_santa_vertical_position += 1

            if character == "v":
                if santa_toggle == True:
                    santa_vertical_position -= 1
                if santa_toggle == False:
                    robo_santa_vertical_position -= 1

            if character == ">":
                if santa_toggle == True:
                    santa_horizontal_position += 1
                if santa_toggle == False:
                    robo_santa_horizontal_position += 1

            if character == "<":
                if santa_toggle == True:
                    santa_horizontal_position -= 1
                if santa_toggle == False:
                    robo_santa_horizontal_position -= 1

            if santa_toggle == True:
                current_position = (
                    santa_horizontal_position,
                    santa_vertical_position,
                )
            if santa_toggle == False:
                current_position = (
                    robo_santa_horizontal_position,
                    robo_santa_vertical_position,
                )

            if current_position in set_of_houses:
                pass
            else:
                set_of_houses.add(current_position)
                total_number_of_houses += 1

            santa_toggle = not santa_toggle

    print(f"The total number of houses visited is: {total_number_of_houses}")

    return total_number_of_houses


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
