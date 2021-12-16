def main():
    input_file = open("./inputs/201501.txt", "r")

    floor = 0

    EOF = False

    while EOF == False:
        current_character = input_file.read(1)

        if current_character == "(":
            floor += 1
        elif current_character == ")":
            floor -= 1
        elif current_character == "":
            EOF = True
        else:
            pass

    # Below is an alternate way to write this.
    # for line in input_file:
    #     for character in line:
    #         if character == '(':
    #             floor += 1
    #         elif character == ')':
    #             floor -= 1
    #         else:
    #             pass

    print(f"The instructions take santa to floor: {floor}")

    input_file.close()


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
