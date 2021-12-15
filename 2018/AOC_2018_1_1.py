from functions import read_lines


def main():

    frequency = 0

    input = read_lines("input201801.txt")

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

    print(frequency)


main()
