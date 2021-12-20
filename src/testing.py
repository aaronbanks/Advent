from .functions import read_lines


def assert_solution_module_expected_output(solution_module):
    """Asserts that a given solution module produces its expected output.

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
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
>>>>>>> f1cd554e7adcbb2d68d890b49c5766aac5db5803
