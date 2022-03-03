def main():

    possible_range = range(367479, 893699)

    possible_passwords_in_range = 0

    for number in possible_range:

        if (
            two_adjacent_the_same(str(number)) == True
            and do_numbers_decrease(str(number)) == False
        ):
            possible_passwords_in_range += 1

    print(
        f"The number of possible passwords in the provided range is: {possible_passwords_in_range}"
    )


def two_adjacent_the_same(str_of_number):

    digit_tracker = 0

    for digit in str_of_number:

        try:
            if digit == str_of_number[digit_tracker + 1]:
                return True
            else:
                pass

        except IndexError:
            pass

        digit_tracker += 1

    return False


def do_numbers_decrease(str_number):

    digit_tracker = 0

    for digit in str_number:

        try:
            if int(str_number[digit_tracker]) <= int(str_number[digit_tracker + 1]):
                pass
            else:
                return True

        except IndexError:
            pass

        digit_tracker += 1

    return False


main()
