def read_lines(file_name):

    return_list = []

    with open(file_name, "r") as input:

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
