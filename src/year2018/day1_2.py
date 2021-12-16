from ..functions import read_lines


def main():

    frequency = 0
    set_of_frequencies = {0}
    first_double = 0

    input = read_lines("./inputs/201801.txt")

    while True:
        for line in input:

            if line[0] == "+":
                modifier_is_positive = True
            elif line[0] == "-":
                modifier_is_positive = False

            line_value = line[1:]

            if modifier_is_positive == True:
                frequency += int(line_value)
            if modifier_is_positive == False:
                frequency -= int(line_value)

            if frequency in set_of_frequencies:
                first_double = frequency
                break

            set_of_frequencies.add(frequency)

        if first_double == frequency:
            break

    print(first_double)


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
