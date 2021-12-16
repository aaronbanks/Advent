def main():
    input_file = open("./inputs/201501.txt", "r")

    floor = 0

    EOF = False

    character_position = 0

    while EOF == False:
        current_character = input_file.read(1)
        character_position += 1

        print(f"The current character position is: {character_position}")
        print(f"The current floor is: {floor}")

        if current_character == "(":
            floor += 1
        elif current_character == ")":
            floor -= 1
        elif current_character == "":
            EOF = True
        else:
            pass

        if floor < 0:
            print(
                f"Santa has entered the basement on character position: {character_position}"
            )
            break

    # Below is an alternate way to write this.
    # for line in input_file:
    #     for character in line:
    #         if character == '(':
    #             floor += 1
    #         elif character == ')':
    #             floor -= 1
    #         else:
    #             pass

    input_file.close()


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
