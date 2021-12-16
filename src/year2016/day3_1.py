from ..functions import read_lines


def main():

    valid_triangle_counter = 0

    input = read_lines("./inputs/201603.txt")

    for triangle in input:

        sides = side_distances(triangle)

        if valid_triangle_calculator(sides[0], sides[1], sides[2]) == True:
            valid_triangle_counter += 1

    print(valid_triangle_counter)


def valid_triangle_calculator(one, two, three):
    if one + two > three and one + three > two and three + two > one:
        return True
    else:
        return False


def side_distances(triangle):
    triangle_values = []

    line_contents = triangle.split()

    for side in line_contents:
        triangle_values.append(int(side))

    return triangle_values


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
