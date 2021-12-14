def main():
    input_file = open('input201502.txt', 'r')

    total_area_required = 0
    current_line = 0

    for line in input_file:
        current_line += 1

        current_line_contents = (line.strip()).split("x", 3)

        length = int(current_line_contents[0])
        width = int(current_line_contents[1])
        height = int(current_line_contents[2])

        side_1 = length * width
        side_2 = width * height
        side_3 = length * height

        sides = [side_1, side_2, side_3]

        smallest_side_area = min(side_1, side_2, side_3)

        required_paper = 2 * sum(sides) + smallest_side_area
        total_area_required += required_paper

        print(f"The surface area required to wrap the gift on line {current_line} is {required_paper} square feet")

    print(f"The total paper required to wrap all the gifts is: {total_area_required}")
    input_file.close()

main()
