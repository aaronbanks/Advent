def main():
    current_line_direction = None
    current_line = 0
    current_line_contents = []

    list_of_forward_directional_inputs = []
    list_of_up_directional_inputs = []
    list_of_down_directional_inputs = []

    input_file = open("input202102.txt", "r")

    for line in input_file:

        current_line += 1

        current_line_contents = (line.strip()).split(" ", 1)

        print(f"Current line #: {current_line}")
        print(f"Current line contents: {current_line_contents}")

        if "forward" in current_line_contents[0]:
            current_line_direction = "forward"
        elif "up" in current_line_contents[0]:
            current_line_direction = "up"
        elif "down" in current_line_contents[0]:
            current_line_direction = "down"
        else:
            current_line_direction = "error"
            print(f"Error on line {current_line}")

        if "forward" in current_line_direction:
            list_of_forward_directional_inputs.append(int(current_line_contents[1]))
        if "up" in current_line_direction:
            list_of_up_directional_inputs.append(int(current_line_contents[1]))
        if "down" in current_line_direction:
            list_of_down_directional_inputs.append(int(current_line_contents[1]))
        else:
            pass

    final_horizontal_position = sum(list_of_forward_directional_inputs)
    final_depth = sum(list_of_down_directional_inputs) - sum(
        list_of_up_directional_inputs
    )

    answer = final_horizontal_position * final_depth

    print(f"The final horizontial position is: {final_horizontal_position}")
    print(f"The final depth is: {final_depth}")
    print(f"The answer to the problem is: {answer}")


main()
