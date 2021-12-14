def main():

    sum = 0

    target_digit_distance = 0
    target_digit_location = 0

    position_on_line = 0

    with open("input201701.txt", "r") as input:

        line = input.readlines()
        clean_line = line[0].strip()

        target_digit_distance = int(len(clean_line) / 2)

        for character in clean_line:
            position_on_line += 1

            if position_on_line + target_digit_distance >= len(clean_line):
                target_digit_location = (
                    (position_on_line + target_digit_distance) - len(clean_line) - 1
                )
            else:
                target_digit_location = position_on_line + target_digit_distance - 1

            if character == clean_line[target_digit_location]:
                sum += int(character)

    print(sum)


main()
