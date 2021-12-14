def main():
    with open('input201702.txt', 'r') as input:

        checksum = 0

        for line in input:

            current_line_as_strs = line.strip().split("\t")
            int_map = map(int, current_line_as_strs)

            current_line_as_ints = list(int_map)

            sorted_list = sorted(current_line_as_ints)
            list_length = len(sorted_list)

            checksum += int(sorted_list[list_length - 1]) - (sorted_list[0])

            print(sorted_list)
            print(int(sorted_list[list_length - 1]) - (sorted_list[0]))

        print(checksum)
main()
