from ..functions import read_lines

from . import day1_1, day1_2, day2_1, day2_2, day3_1, day3_2


def test_all():
    for solution_module in (day1_1, day1_2, day2_1, day2_2, day3_1, day3_2):
        if solution_module.expected_output is None:
            # Need an expected value to test
            continue

        input_lines = read_lines(solution_module.input_filename)
        output = solution_module.solution(input_lines)
        assert (
            output == solution_module.expected_output
        ), f"{solution_module.__name__}: actual output ({output!r}) did not match expected output ({solution_module.expected_output!r})."
