def main():
    input_file = open("input201502.txt", "r")

    current_line = 0

    total_ribbon_needed = 0

    for line in input_file:
        current_line += 1

        current_line_contents = (line.strip()).split("x", 3)

        length = int(current_line_contents[0])
        width = int(current_line_contents[1])
        height = int(current_line_contents[2])

        dimensions = [length, width, height]

        ribbon_for_bow = length * width * height
        # print(ribbon_for_bow)

        ribbon_for_wrap = 2 * sum(sorted(dimensions)[0:2])

        # print(ribbon_for_wrap)

        total_ribbon_needed += ribbon_for_bow + ribbon_for_wrap

    print(f"Total ribbon needed is: {total_ribbon_needed}")

    input_file.close()


main()
