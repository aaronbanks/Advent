from ..functions import run_solution

input_filename = "./inputs/201702.txt"
expected_output = 303


def solution(input_lines):

    checksum = 0

    for line in input_lines:

        current_line_as_strs = line.strip().split("\t")
        current_line_as_ints = list(map(int, current_line_as_strs))

        list_length = len(current_line_as_ints)

        for number_1 in current_line_as_ints:
            line_solved = False

            for number_2 in current_line_as_ints:

                if number_1 == number_2:
                    continue

                if number_1 % number_2 == 0:
                    checksum += number_1 / number_2
                    line_solved = True
                    break

            if line_solved == True:
                break

    result = int(checksum)
    print(result)
    return result


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
