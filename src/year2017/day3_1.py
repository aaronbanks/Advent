from ..functions import run_solution

input_filename = "./inputs/201703.txt"
expected_output = 480


def solution(input_lines):
    input = int(input_lines[0])

    previous_perimeter_end = 0
    current_perimeter_level = 0

    current_perimeter_size = 0

    for number in range(1, input + 1):
        if number >= current_perimeter_size + previous_perimeter_end:
            previous_perimeter_end = number
            current_perimeter_level += 1
            current_perimeter_size += 8

    location_of_input = location_calculator(
        current_perimeter_level, previous_perimeter_end, input
    )

    steps_to_port = abs(location_of_input[0]) + abs(location_of_input[1])
    print(steps_to_port)
    return steps_to_port


def location_calculator(current_perimeter_level, previous_perimeter_end, input_value):

    perimeter_start_location = [
        current_perimeter_level,
        (current_perimeter_level * -1) + 1,
    ]
    print(perimeter_start_location)

    difference = input_value - (previous_perimeter_end + 1)
    if difference == 0:
        return perimeter_start_location

    distance_to_top = current_perimeter_level * 2 - 1
    distance_across_sides = current_perimeter_level * 2

    movment_counter = 1

    for x in range(1, difference + 1):
        if movment_counter <= distance_to_top:
            perimeter_start_location[1] += 1

        elif movment_counter <= distance_to_top + distance_across_sides:
            perimeter_start_location[0] -= 1

        elif movment_counter <= distance_to_top + distance_across_sides * 2:
            perimeter_start_location[1] -= 1

        else:
            perimeter_start_location[0] += 1

        movment_counter += 1

    return perimeter_start_location


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
