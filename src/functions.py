from . import viz

import sys


def read_lines(file_name):
    """Reads all of the lines from a text file into an list of strings.

    Leading and trailing whitespace is stripped.
    """

    return_list = []

    with open(file_name, "rt") as input:

        for line in input:
            return_list.append(line.strip())

    return return_list


def run_solution(solution_function, input_filename, expected_output=None):
    input_lines = read_lines(input_filename)
    output = solution_function(input_lines)

    if expected_output is None:
        print(f"{output!r}")
    else:
        # If an expected value was provided, indicate whether it matches.
        if output == expected_output:
            print(f"{output!r} (matches expected value)")
        else:
            print(f"{output!r} (does not match expected output {expected_output!r})")

    if "--viz" in sys.argv:
        viz.show()


def read_input_and_store_values_in_nested_list(input_lines):
    nested_list_containing_input = []

    for line in input_lines:

        current_line_contents = []

        for character in line:
            current_line_contents.append(character)

        nested_list_containing_input.append(current_line_contents)

    return nested_list_containing_input
