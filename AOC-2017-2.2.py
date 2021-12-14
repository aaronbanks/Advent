def main():
    with open('input201702.txt', 'r') as input:

        checksum = 0

        for line in input:

            current_line_as_strs = line.strip().split("\t")
            current_line_as_ints = list(map(int, current_line_as_strs))

            list_length = len(current_line_as_ints)

            for number_1 in current_line_as_ints:
                line_solved = False

                for number_2 in current_line_as_ints:

                    if number_1 == number_2:
                        continue

                    if number_1 % number_2 == 0:
                        checksum += number_1 / number_2
                        line_solved = True
                        break

                if line_solved == True:
                    break

        print(int(checksum))

main()
