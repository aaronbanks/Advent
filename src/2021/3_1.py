def main():

    input_file = open("./inputs/202103.txt", "r")

    current_line = 0
    length_of_lines = 0

    nested_list_storing_all_input_digits = []

    binary_gamma_rate = []
    binary_epsilon_rate = []

    gamma_conversion = 0
    epsilon_conversion = 0

    decimal_gamma_rate = 0
    decimal_epsilon_rate = 0

    power_consumption = 0

    # This loop goes through each line of the file and stores it's values in a list of list
    # THIS APPEARS TO EXECUTE AS PLANNED
    for line in input_file:

        current_line += 1

        current_line_contents = []

        for z in line.strip():
            current_line_contents.append(z)

        if current_line == 1:
            for digit in current_line_contents:
                nested_list_storing_all_input_digits.append([digit])
                length_of_lines += 1

        else:
            position_on_line = 0
            for digit in current_line_contents:

                nested_list_storing_all_input_digits[position_on_line].append(digit)
                position_on_line += 1

    print("Below is all the input data, stored in a list of list:")
    print(nested_list_storing_all_input_digits)

    # This loop reads the stored input data and converts to binary gama na depsilon rates
    for element in nested_list_storing_all_input_digits:
        number_of_ones = 0
        number_of_zeros = 0

        for x in element:
            if int(x) == 1:
                number_of_ones += 1
            if int(x) == 0:
                number_of_zeros += 1

        if number_of_ones > number_of_zeros:
            binary_gamma_rate.append(1)
            binary_epsilon_rate.append(0)

        elif number_of_ones < number_of_zeros:
            binary_gamma_rate.append(0)
            binary_epsilon_rate.append(1)

    print(f"The binary gamma rate is: {binary_gamma_rate}")
    print(f"The binary epsilon rate is: {binary_epsilon_rate}")

    # This loop reads the binary_gamma_rate and converts it to decimal_gamma_rate
    conversion_counter = 0

    for digit in binary_gamma_rate:
        conversion_counter += 1
        gamma_conversion += digit * (2 ** (length_of_lines - conversion_counter))

    decimal_gamma_rate = gamma_conversion
    print(f"The decimal gamma rate is: {decimal_gamma_rate}")

    # This loop reads the binary_epsilon_rate and converts it to decimal_epsilon_rate
    conversion_counter = 0

    for digit in binary_epsilon_rate:
        conversion_counter += 1
        epsilon_conversion += digit * (2 ** (length_of_lines - conversion_counter))

    decimal_epsilon_rate = epsilon_conversion
    print(f"The decimal epsilon rate is: {decimal_epsilon_rate}")

    # simple calculation to find answer:
    power_consumption = decimal_gamma_rate * decimal_epsilon_rate

    print(f"The power power consumption of the submarine i: {power_consumption}")


main()
