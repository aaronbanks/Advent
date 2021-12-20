from ..functions import run_solution
import copy

input_filename = "./inputs/202103_test.txt"
expected_output = None

def solution(input_lines):

    nested_list_storing_all_input_digits = read_input_store_values(input_lines)

    print(f"nested_list_storing_all_input_digits: {nested_list_storing_all_input_digits}")

    calculate_oxygen_rating = copy.copy(nested_list_storing_all_input_digits)
    calculate_c02_rating = copy.copy(nested_list_storing_all_input_digits)

    # iterate through each digit, diritmine which lines should be deleted and then delete them.
    binary_oxygen_rating = determine_and_delete_digits_from_oxygen(calculate_oxygen_rating)
    binary_c02_rating  = determine_and_delete_digits_from_c02(calculate_c02_rating)

    print(f"The oxygen generator rating in binary is: {binary_oxygen_rating}")
    print(f"The C02 scrubber ratting in binary is: {binary_c02_rating}")


# This function goes through each line of the file and stores each digit seperately in a list of list
def read_input_store_values(input_lines):
    nested_list_storing_all_input_digits = []
    first_line = True

    for line in input_lines:

        current_line_contents = []

        for character in line:
            current_line_contents.append(int(character))

        #Create a list for each bit in line
        if first_line == True:
            for digit in current_line_contents:
                nested_list_storing_all_input_digits.append([digit])
            first_line == False

        #Populate lists with each bit in subsequent lines
        else:
            position_on_line = 0
            for digit in current_line_contents:
                nested_list_storing_all_input_digits[position_on_line].append(digit)
                position_on_line += 1
        print(nested_list_storing_all_input_digits)

    return nested_list_storing_all_input_digits

def determine_and_delete_digits_from_oxygen(calculate_oxygen_rating):
    for element in calculate_oxygen_rating:
        # calculate the nmber of 1s and 0s at this digit
        number_of_ones = 0
        number_of_zeros = 0

        for x in element:
            if x == 1:
                number_of_ones += 1
            if x == 0:
                number_of_zeros += 1

        positions_to_be_deleted_from_oxygen = []

        # make lists of which lines need to be deleted
        counter = -1
        if number_of_ones >= number_of_zeros:
            for n in element:
                counter += 1
                if n == 0:
                    positions_to_be_deleted_from_oxygen.append(counter)
        else:
            for n in element:
                counter += 1
                if n == 1:
                    positions_to_be_deleted_from_oxygen.append(counter)

        # delete all the positions that you detirmined should be deleted
        #reversing the order means you start from the highest number and don't need to adjust anything as you go
        for position in reversed(positions_to_be_deleted_from_oxygen):
            for b in calculate_oxygen_rating:
                del b[position]

        # if len(calculate_oxygen_rating[0]) == 1:
        #     return calculate_oxygen_rating
        #     break

    return calculate_oxygen_rating

def determine_and_delete_digits_from_c02(calculate_c02_rating):
    for element in calculate_c02_rating:

        number_of_ones = 0
        number_of_zeros = 0

        for x in element:
            if x == 1:
                number_of_ones += 1
            if x == 0:
                number_of_zeros += 1

        positions_to_be_deleted_from_c02 = []

        counter = -1
        if number_of_zeros >= number_of_ones:
            for n in element:
                counter += 1
                if n == 1:
                    positions_to_be_deleted_from_c02.append(counter)
        else:
            for n in element:
                counter += 1
                if n == 0:
                    positions_to_be_deleted_from_c02.append(counter)

        for position in reversed(positions_to_be_deleted_from_c02):
            for b in calculate_c02_rating:
                del b[position]

        # if len(calculate_c02_rating[0]) == 1:
        #     return calculate_c02_rating
        #     break

    return calculate_c02_rating

if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
