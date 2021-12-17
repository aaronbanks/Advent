def read_lines(file_name):
    """Reads all of the lines from a text file into an list of strings.

    Leading and trailing whitespace is stripped.
    """

    return_list = []

    with open(file_name, "rt") as input:

        for line in input:
            return_list.append(line.strip())

    return return_list


def run_solution(solution_function, input_filename, expected=None):
    input_lines = read_lines(input_filename)

    result = solution_function(input_lines)

    if expected is None:
        print(f"{result!r}")
    else:
        # If an expected value was provided, indicate whether it matches.
        if result == expected:
            print(f"{result!r} (matches expected value)")
        else:
            print(f"{result!r} (does not match expected value {expected!r})")


def assert_solution_module_expected_output(solution_module):
    """Asserts that a given solution module produces its expected output.

    Has no effect unless the module exports a non-None .expected_output property.
    """

    if getattr(solution_module, "expected_output", None) is None:
        print(
            f"Ignoring {solution_module.__name__} as it doesn't export any .expected_output property."
        )
        return

    input_lines = read_lines(solution_module.input_filename)
    output = solution_module.solution(input_lines)
    assert (
        output == solution_module.expected_output
    ), f"{solution_module.__name__}: actual output ({output!r}) did not match expected output ({solution_module.expected_output!r})."
