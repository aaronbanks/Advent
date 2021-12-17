from ..functions import run_solution

input_filename = "./inputs/202103.txt"
expected_output = None


def solution(input_lines):

    current_line = 0
    length_of_lines = 0

    nested_list_storing_all_input_digits = []

    # This loop goes through each line of the file and stores it's values in a list of list
    for line in input_lines:

        current_line += 1

        current_line_contents = []

        for z in line.strip():
            current_line_contents.append(int(z))

        if current_line == 1:
            for digit in current_line_contents:
                nested_list_storing_all_input_digits.append([int(digit)])
                length_of_lines += 1

        else:
            position_on_line = 0
            for digit in current_line_contents:

                nested_list_storing_all_input_digits[position_on_line].append(digit)
                position_on_line += 1

    # print("Below is all the input data, stored in a list of list:")
    # print(nested_list_storing_all_input_digits)

    calculate_oxygen_rating = nested_list_storing_all_input_digits
    calculate_c02_rating = nested_list_storing_all_input_digits

    # iterate through each digit, diritmine which lines should be deleted and then delete them.
    for element in nested_list_storing_all_input_digits:

        # calculate the nmber of 1s and 0s at this digit
        number_of_ones = 0
        number_of_zeros = 0

        for x in element:
            if x == 1:
                number_of_ones += 1
            if x == 0:
                number_of_zeros += 1

        positions_to_be_deleted_from_oxygen = []
        positions_to_be_deleted_from_c02 = []

        # make lists of which lines need to be deleted
        if number_of_ones >= number_of_zeros:

            counter = -1

            for n in element:
                counter += 1

                if n == 0:
                    positions_to_be_deleted_from_oxygen.append(counter)
                if n == 1:
                    positions_to_be_deleted_from_c02.append(counter)

        if number_of_ones < number_of_zeros:

            counter = -1

            for n in element:
                counter += 1

                if n == 0:
                    positions_to_be_deleted_from_c02.append(counter)
                if n == 1:
                    positions_to_be_deleted_from_oxygen.append(counter)

        positions_deleted = 0

        # delete all the positions that you detirmined should be deleted
        for position in positions_to_be_deleted_from_oxygen:

            for b in calculate_oxygen_rating:
                del b[position - positions_deleted]

            positions_deleted += 1

        positions_deleted = 0

        for position in positions_to_be_deleted_from_c02:

            for b in calculate_c02_rating:
                del b[position - positions_deleted]

            positions_deleted += 1

    print(f"The oxygen generator rating in binary is: {calculate_oxygen_rating}")
    print(f"The C02 scrubber ratting in binary is: {calculate_c02_rating}")


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
