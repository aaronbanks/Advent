from ..functions import run_solution

input_filename = "./inputs/201802.txt"
expected_output = 5434


def solution(input_lines):

    checksum = 0
    boxes_with_two_of_same = 0
    boxes_with_three_of_same = 0

    for line in input_lines:

        set_of_characters_counted = set()

        box_has_two_of_same = False
        box_has_three_of_same = False

        for character in line:
            if character in set_of_characters_counted:
                continue

            set_of_characters_counted.add(character)

            counter = line.count(character)

            if counter == 2 and box_has_two_of_same == False:
                boxes_with_two_of_same += 1
                box_has_two_of_same = True

            if counter == 3 and box_has_three_of_same == False:
                boxes_with_three_of_same += 1
                box_has_three_of_same == True

    checksum = boxes_with_two_of_same * boxes_with_three_of_same
    print(checksum)
    return checksum


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
