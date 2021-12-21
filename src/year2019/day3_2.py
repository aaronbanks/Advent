from ..functions import run_solution

input_filename = "./inputs/201903.txt"
expected_output = 32132


def solution(input_lines):
    set_of_first_wire_locations = set()
    set_of_crossing_wire_locations = set()

    wire_count = 0

    for wire in input_lines:
        wire_count += 1

        if wire_count == 1:
            set_of_first_wire_locations = analyze_wire_one(wire)

        if wire_count == 2:
            set_of_crossing_wire_locations = analyze_wire_two(
                wire, set_of_first_wire_locations
            )

    wire_crossing_locations = list(set_of_crossing_wire_locations)

    wire_count = 0

    wire_one_crossing_distances = {}
    wire_two_crossing_distances = {}

    for wire in input_lines:
        wire_count += 1

        if wire_count == 1:
            wire_one_crossing_distances = find_distance_to_each_crossing(
                wire, wire_crossing_locations
            )
        if wire_count == 2:
            wire_two_crossing_distances = find_distance_to_each_crossing(
                wire, wire_crossing_locations
            )

    combined_distance_to_crossing = {}

    for crossing in wire_crossing_locations:
        combined_distance_to_crossing[crossing] = (
            wire_one_crossing_distances[crossing]
            + wire_two_crossing_distances[crossing]
        )

    lowest_combined_steps = None

    for key in combined_distance_to_crossing:
        try:
            if combined_distance_to_crossing[key] < lowest_combined_steps:
                lowest_combined_steps = combined_distance_to_crossing[key]
        except TypeError:
            lowest_combined_steps = combined_distance_to_crossing[key]

    return lowest_combined_steps


def find_distance_to_each_crossing(wire, wire_crossing_locations):

    dict_of_crossing_distances = {}

    current_x_coordinate = 0
    current_y_coordinate = 0

    distance_traveled_on_wire = 0

    list_of_line_contents = wire.split(",")

    for direction in list_of_line_contents:

        direction_modifier = direction[0]
        movement_value = int(direction[1:])

        if direction_modifier == "U":
            for move in range(movement_value):
                current_y_coordinate += 1
                distance_traveled_on_wire += 1
                current_location = (current_x_coordinate, current_y_coordinate)

                if current_location in wire_crossing_locations:
                    location_counter = -1

                    for location in wire_crossing_locations:
                        location_counter += 1
                        if location == current_location:
                            dict_of_crossing_distances[
                                location
                            ] = distance_traveled_on_wire

        elif direction_modifier == "D":
            for move in range(movement_value):
                current_y_coordinate -= 1
                distance_traveled_on_wire += 1
                current_location = (current_x_coordinate, current_y_coordinate)

                if current_location in wire_crossing_locations:
                    location_counter = -1

                    for location in wire_crossing_locations:
                        location_counter += 1
                        if location == current_location:
                            dict_of_crossing_distances[
                                location
                            ] = distance_traveled_on_wire

        elif direction_modifier == "L":
            for move in range(movement_value):
                current_x_coordinate -= 1
                distance_traveled_on_wire += 1
                current_location = (current_x_coordinate, current_y_coordinate)

                if current_location in wire_crossing_locations:
                    location_counter = -1

                    for location in wire_crossing_locations:
                        location_counter += 1
                        if location == current_location:
                            dict_of_crossing_distances[
                                location
                            ] = distance_traveled_on_wire

        elif direction_modifier == "R":
            for move in range(movement_value):
                current_x_coordinate += 1
                distance_traveled_on_wire += 1
                current_location = (current_x_coordinate, current_y_coordinate)

                if current_location in wire_crossing_locations:
                    location_counter = -1

                    for location in wire_crossing_locations:
                        location_counter += 1
                        if location == current_location:
                            dict_of_crossing_distances[
                                location
                            ] = distance_traveled_on_wire

    return dict_of_crossing_distances


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
