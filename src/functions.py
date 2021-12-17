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

    assert output == solution_module.expected_output, (
        f"{solution_module.__name__}: actual output ({output!r}) did not match "
        f"expected output ({solution_module.expected_output!r})."
    )
