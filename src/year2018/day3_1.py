from ..functions import run_solution

input_filename = "./inputs/201803.txt"
expected_output = None

# ANSWER 84013 is too low
# ANSWER 117127 is too high


def solution(input_lines):

    list_of_component_tuples = extract_components_of_lines(input_lines)

    square_inches_with_overlapping_claim = determine_locations_with_overlapping_claims(
        list_of_component_tuples
    )

    return square_inches_with_overlapping_claim


def determine_locations_with_overlapping_claims(set_of_component_tuples):

    locations_claimed = set()
    locations_with_overlapping_claims = set()

    print("set of", set_of_component_tuples)

    for _number, offset, dimensions in set_of_component_tuples:
        current_x_coordinate, current_y_coordinate = offset

        for x_modifier in range(dimensions[0]):
            for y_modifier in range(dimensions[1]):
                adjusted_coordinates = (
                    current_x_coordinate + x_modifier,
                    current_y_coordinate + y_modifier,
                )

                if (
                    adjusted_coordinates in locations_claimed
                    and adjusted_coordinates not in locations_with_overlapping_claims
                ):
                    locations_with_overlapping_claims.add(adjusted_coordinates)
                else:
                    locations_claimed.add(adjusted_coordinates)

    return len(locations_with_overlapping_claims)


def extract_components_of_lines(input_lines):

    set_of_component_tuples = set()

    for line in input_lines:
        line_components = line.split()
        line_components.pop(1)

        id_component = int(line_components[0].strip("#"))

        starting_corner_values = line_components[1].strip(":").split(",")
        starting_corner_component = (
            int(starting_corner_values[0]),
            int(starting_corner_values[1]),
        )

        sides_compenent_values = line_components[2].split("x")
        sides_component = (
            int(sides_compenent_values[0]),
            int(sides_compenent_values[1]),
        )

        component_tuple = (id_component, starting_corner_component, sides_component)

        set_of_component_tuples.add(component_tuple)

    return set_of_component_tuples


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
