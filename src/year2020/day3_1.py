from .. import viz
from ..functions import run_solution, read_input_and_store_values_in_nested_list

input_filename = "./inputs/202003.txt"
expected_output = 198


def solution(input_lines):
    trees_encountered_on_path = 0

    slope = (3, 1)

    first_line = True

    distance_to_bottom = 0

    for line in input_lines:
        distance_to_bottom += 1

    nested_list_containing_input = read_input_and_store_values_in_nested_list(
        input_lines
    )

    current_line_count = 2
    current_location_on_line = 0

    all_trees_layer = viz.new_layer(color="green", z=-1)

    for line in nested_list_containing_input:
        for location, character in enumerate(line):
            if character == "#":
                all_trees_layer.dot_at(location, current_line_count)

        if first_line == True:
            line[current_location_on_line] = "O"
            first_line = False
            continue

        current_location_on_line += slope[0]
        current_location_on_line = current_location_on_line % len(line)

        viz.line_to(current_location_on_line, current_line_count)
        if line[current_location_on_line] == "#":
            trees_encountered_on_path += 1
            line[current_location_on_line] = "X"
            viz.dot_at(current_location_on_line, current_line_count)
        else:
            line[current_location_on_line] = "O"

        current_line_count += 1

    print(f"trees_encountered_on_path: {trees_encountered_on_path}")

    return trees_encountered_on_path


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
