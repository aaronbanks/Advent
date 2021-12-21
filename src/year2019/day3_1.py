from ..functions import run_solution

input_filename = "./inputs/201903.txt"
expected_output = None


# ANSWER 5567 is too high
def solution(input_lines):
    set_of_first_wire_locations = set()

    set_of_crossing_wire_locations = set()

    list_of_distances_to_port = []

    wire_count = 0

    for wire in input_lines:
        wire_count += 1

        if wire_count == 1:
            set_of_first_wire_locations = analyze_wire_one(wire)

        if wire_count == 2:
            set_of_crossing_wire_locations = analyze_wire_two(wire, set_of_first_wire_locations)

    for location in set_of_crossing_wire_locations:
        disatnce_to_port = abs(location[0]) + abs(location[1])
        list_of_distances_to_port.append(disatnce_to_port)

    answer = max(list_of_distances_to_port)
    print(answer)

def analyze_wire_one(wire):
    current_x_coordinate = 0
    current_y_coordinate = 0

    set_of_wire_locations = set()

    list_of_line_contents = wire.split(",")

    for direction in list_of_line_contents:

        direction_modifier = direction[0]
        movement_value = int(direction[1:])

        if direction_modifier == "U":
            for move in range(movement_value):
                current_y_coordinate += 1
                current_location = (current_x_coordinate, current_y_coordinate)
                set_of_wire_locations.add(current_location)

        elif direction_modifier == "D":
            for move in range(movement_value):
                current_y_coordinate -= 1
                current_location = (current_x_coordinate, current_y_coordinate)
                set_of_wire_locations.add(current_location)

        elif direction_modifier == "L":
            for move in range(movement_value):
                current_x_coordinate -= 1
                current_location = (current_x_coordinate, current_y_coordinate)
                set_of_wire_locations.add(current_location)

        elif direction_modifier == "R":
            for move in range(movement_value):
                current_x_coordinate += 1
                current_location = (current_x_coordinate, current_y_coordinate)
                set_of_wire_locations.add(current_location)

    return set_of_wire_locations

def analyze_wire_two(wire, set_of_first_wire_locations):
    current_x_coordinate = 0
    current_y_coordinate = 0

    crossing_wire_locations = set()

    list_of_line_contents = wire.split(",")

    for direction in list_of_line_contents:

        direction_modifier = direction[0]
        movement_value = int(direction[1:])

        if direction_modifier == "U":
            for move in range(movement_value):
                current_y_coordinate += 1
                current_location = (current_x_coordinate, current_y_coordinate)
                if current_location in set_of_first_wire_locations:
                    crossing_wire_locations.add(current_location)

        elif direction_modifier == "D":
            for move in range(movement_value):
                current_y_coordinate -= 1
                current_location = (current_x_coordinate, current_y_coordinate)
                if current_location in set_of_first_wire_locations:
                    crossing_wire_locations.add(current_location)

        elif direction_modifier == "L":
            for move in range(movement_value):
                current_x_coordinate -= 1
                current_location = (current_x_coordinate, current_y_coordinate)
                if current_location in set_of_first_wire_locations:
                    crossing_wire_locations.add(current_location)

        elif direction_modifier == "R":
            for move in range(movement_value):
                current_x_coordinate += 1
                current_location = (current_x_coordinate, current_y_coordinate)
                if current_location in set_of_first_wire_locations:
                    crossing_wire_locations.add(current_location)

    return crossing_wire_locations

if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
