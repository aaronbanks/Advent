from ..functions import run_solution

input_filename = "./inputs/202001.txt"
expected_output = 299299


def solution(input_lines):

    input = list(map(int, input_lines))

    value_1 = 0
    value_2 = 0

    solved = False

    for value in input:

        for values in input:

            if value + values == 2020:
                value_1 = value
                value_2 = values
                solved = True
                print(value_1)
                print(value_2)
                break

        if solved == True:
            break

    result = value_1 * value_2
    print(result)
    return result


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
