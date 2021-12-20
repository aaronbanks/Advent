__package__ = "src.year2018"

from ..testing import assert_solution_module_expected_output

from . import (
    day1_1,
    day1_2,
    day2_1,
    day2_2,
)


def test_2018():
    for solution_module in (
        day1_1,
        day1_2,
        day2_1,
        day2_2,
    ):
        assert_solution_module_expected_output(solution_module)
