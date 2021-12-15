def main():

    keypad = (
        ("X", "X", "1", "X", "X"),
        ("X", "2", "3", "4", "X"),
        ("5", "6", "7", "8", "9"),
        ("X", "A", "B", "C", "X"),
        ("X", "X", "D", "X", "X"),
    )

    current_keypad_location = [2, 1]

    bathroom_code = []

    with open("input201602.txt", "r") as input:

        for line in input:
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

                if (
                    keypad[current_keypad_location[0]][current_keypad_location[1]]
                    == "X"
                ):
                    current_keypad_location = previous_keypad_location

            print(current_keypad_location)
            bathroom_code.append(
                keypad[current_keypad_location[0]][current_keypad_location[1]]
            )

        print(f"The bathroom code is: {bathroom_code}")


main()
