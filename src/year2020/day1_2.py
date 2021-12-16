from ..functions import read_lines


def main():

    input = list(map(int, read_lines("./inputs/202001.txt")))

    value_1 = 0
    value_2 = 0
    value_3 = 0

    solved = False

    for value in input:
        for values in input:
            for valuess in input:

                if value + values + valuess == 2020:
                    value_1 = value
                    value_2 = values
                    value_3 = valuess

                    solved = True

                    print(value_1)
                    print(value_2)
                    print(value_3)

                    break

            if solved == True:
                break

    print(value_1 * value_2 * value_3)


main()
