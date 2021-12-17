from ..functions import run_solution

input_filename = "./inputs/201702.txt"
expected_output = 41919


def solution(input_lines):

    checksum = 0

    for line in input_lines:

        current_line_as_strs = line.strip().split("\t")
        int_map = map(int, current_line_as_strs)

        current_line_as_ints = list(int_map)

        sorted_list = sorted(current_line_as_ints)
        list_length = len(sorted_list)

        checksum += int(sorted_list[list_length - 1]) - (sorted_list[0])

        print(sorted_list)
        print(int(sorted_list[list_length - 1]) - (sorted_list[0]))

    print(checksum)

    return checksum


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
