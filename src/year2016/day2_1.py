def main():

    keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

    current_keypad_location = [1, 1]

    bathroom_code = []

    with open("./inputs/201602.txt", "r") as input:

        for line in input:
            current_line_contents = line.strip()

            for character in current_line_contents:

                if character == "L":
                    if current_keypad_location[1] == 0:
                        pass
                    else:
                        current_keypad_location[1] -= 1

                if character == "R":
                    if current_keypad_location[1] == 2:
                        pass
                    else:
                        current_keypad_location[1] += 1

                if character == "U":
                    if current_keypad_location[0] == 0:
                        pass
                    else:
                        current_keypad_location[0] -= 1

                if character == "D":
                    if current_keypad_location[0] == 2:
                        pass
                    else:
                        current_keypad_location[0] += 1

            print(current_keypad_location)
            bathroom_code.append(
                keypad[current_keypad_location[0]][current_keypad_location[1]]
            )

        print(f"The bathroom code is: {bathroom_code}")


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
