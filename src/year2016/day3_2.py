from ..functions import run_solution

input_filename = "./inputs/201603.txt"
expected_output = None


def solution(input_lines):

    valid_triangle_counter = 0

    list_of_triangles = []

    current_tri_one = []
    current_tri_two = []
    current_tri_three = []

    tri_completion_counter = 0

    for line in input_lines:
        if tri_completion_counter >= 3:

            tri_completion_counter = 0

            list_of_triangles.append(current_tri_one)
            list_of_triangles.append(current_tri_two)
            list_of_triangles.append(current_tri_three)

            current_tri_one = []
            current_tri_two = []
            current_tri_three = []

        line_values = []

        line_contents = line.split()

        for side in line_contents:
            line_values.append(int(side))

        current_tri_one.append(line_values[0])
        current_tri_two.append(line_values[1])
        current_tri_three.append(line_values[2])

        tri_completion_counter += 1

    list_of_triangles.append(current_tri_one)
    list_of_triangles.append(current_tri_two)
    list_of_triangles.append(current_tri_three)

    # print(list_of_triangles)
    for triangle in list_of_triangles:
        if valid_triangle_calculator(triangle[0], triangle[1], triangle[2]) == True:
            valid_triangle_counter += 1

    print(valid_triangle_counter)
    return valid_triangle_counter


def valid_triangle_calculator(one, two, three):
    if one + two > three and one + three > two and three + two > one:
        return True
    else:
        return False


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
