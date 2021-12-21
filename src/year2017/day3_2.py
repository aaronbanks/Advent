from .. import viz

from ..functions import run_solution

input_filename = "./inputs/201703.txt"
expected_output = 32


def solution(input_lines):
    input = int(input_lines[0])

    grid_positions_values = {(0, 0): 1}
    viz.dot_at(0, 0)
    viz.move_to(0, 0)

    previous_perimeter_end = 1
    current_perimeter_level = 0
    current_perimeter_size = 0

    position_counter = 1

    current_x_coordinate = 1
    current_y_coordinate = 0

    while True:
        viz.line_to(current_x_coordinate, current_y_coordinate)

        position_counter += 1

        # 1# CALCULATE_CURRENT_POSITION's_VALUE BASED ON SURROUNDING COORDINATES
        current_position_value = value_of_surrounding_coordinates(
            current_x_coordinate, current_y_coordinate, grid_positions_values
        )

        # 2# CREATE NEW LOCATION IN GRID POSITION AND ASSIGN VALUE TO GRID POSITION
        grid_positions_values[
            (current_x_coordinate, current_y_coordinate)
        ] = current_position_value

        # 3# THIS IS THE CONDITION FOR ANSWERING THIS QUESTION
        if current_position_value > input:
            print(f"First value larger than the input: {current_position_value}")
            break

        # 4# MOVE TO THE NEXT POSITION IN THE SPIRAL
        if position_counter > current_perimeter_size + previous_perimeter_end:
            previous_perimeter_end = position_counter - 1
            current_perimeter_level += 1
            current_perimeter_size += 8
            perimeter_move_counter = 0

        distance_to_top = current_perimeter_level * 2 - 1
        distance_across_sides = current_perimeter_level * 2

        if perimeter_move_counter < distance_to_top:
            current_y_coordinate += 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides:
            current_x_coordinate -= 1

        elif perimeter_move_counter < distance_to_top + distance_across_sides * 2:
            current_y_coordinate -= 1

        else:
            current_x_coordinate += 1

        perimeter_move_counter += 1

    return current_perimeter_size


def value_of_surrounding_coordinates(
    current_x_coordinate, current_y_coordinate, grid_positions_values
):
    value_counter = 0

    for x_modifier in [-1, 0, +1]:
        for y_modifier in [-1, 0, +1]:
            if x_modifier == 0 and y_modifier == 0:
                continue

            x = current_x_coordinate + x_modifier
            y = current_y_coordinate + y_modifier

            value_counter += grid_positions_values.get((x, y), 0)

            viz.point_at(x, y)
    return value_counter


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
