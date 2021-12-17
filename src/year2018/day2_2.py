from ..functions import run_solution

input_filename = "./inputs/201802.txt"
expected_output = "agimdjvlhedpsyoqfzuknpjwt"


def solution(input_lines):

    shared_characters = ""
    for line in input_lines:

        box_pair_found = False

        current_line_content = []

        for character in line:
            current_line_content.append(character)

        for lines in input_lines:

            if lines == line:
                continue

            number_of_differences = 0
            list_of_shared_characters = []

            character_counter = -1

            for characters in lines:

                character_counter += 1

                if characters == current_line_content[character_counter]:
                    list_of_shared_characters.append(characters)
                else:
                    number_of_differences += 1

            if number_of_differences == 1:
                shared_characters = "".join(list_of_shared_characters)
                print(shared_characters)
                box_pair_found = True
                break

        if box_pair_found == True:
            break

    return shared_characters


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
