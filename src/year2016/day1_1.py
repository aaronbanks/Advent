from .. import viz
from ..functions import run_solution

input_filename = "./inputs/201601.txt"
expected_output = 209


def solution(input_lines):

    current_compass_direction = "N"
    list_of_compass_directions = ("N", "E", "S", "W")

    compass_direction_value = 0

    horizontal_position = 0
    vertical_position = 0

    with open("./inputs/201601.txt", "r") as input:

        for line in input:
            current_line_contents = (line.strip()).split(", ")

            for instruction in current_line_contents:

                if instruction[:1] == "R":
                    compass_direction_value += 1
                    if compass_direction_value > 3:
                        compass_direction_value = 0

                elif instruction[:1] == "L":
                    compass_direction_value -= 1
                    if compass_direction_value < 0:
                        compass_direction_value = 3

                current_compass_direction = list_of_compass_directions[
                    compass_direction_value
                ]

                if current_compass_direction == "N":
                    vertical_position += int(instruction[1:])

                elif current_compass_direction == "E":
                    horizontal_position += int(instruction[1:])

                elif current_compass_direction == "S":
                    vertical_position -= int(instruction[1:])

                elif current_compass_direction == "W":
                    horizontal_position -= int(instruction[1:])

                viz.line_to(horizontal_position, vertical_position)

    distance_to_destination = abs(vertical_position) + abs(horizontal_position)
    print(f"The shortest path to the destination is {distance_to_destination} blocks")
    return distance_to_destination


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
