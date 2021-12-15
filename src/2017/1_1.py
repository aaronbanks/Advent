def main():

    with open("./inputs/201701.txt", "r") as input:

        sum_of_digits = 0

        location_on_line = 0

        first_character_on_line = ""

        input_line = input.readlines()
        input.seek(0)

        for character in input_line[0]:

            current_digits = input.readline(2)

            location_on_line += 1

            input.seek(location_on_line)

            if location_on_line == 1:
                first_character_on_line = character

            if location_on_line == len(input_line[0]) - 1:
                if character == first_character_on_line:
                    sum_of_digits += int(first_character_on_line)
                break

            if current_digits[0] == current_digits[1]:
                sum_of_digits += int(current_digits[0])

        print(sum_of_digits)


main()
