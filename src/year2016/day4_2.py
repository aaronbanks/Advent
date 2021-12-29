from pprint import pprint
from ..functions import run_solution

input_filename = "./inputs/201604.txt"
expected_output = 173787


def solution(input_lines):

    sum_of_sector_ids_from_real_rooms = 0

    for line in input_lines:

        line_contents = line.split("-")

        number_of_chunks = len(line_contents)
        chunk_counter = 0

        five_most_common_characters = []
        sector_id = 0
        checksum = 0

        is_real_room = False

        dict_of_letter_and_repetition_pairs = {}

        for chunk in line_contents:

            chunk_counter += 1

            if chunk_counter == number_of_chunks:

                sorted_dict = sorted(dict_of_letter_and_repetition_pairs.items(), key=lambda x: (-x[1], x[0]))

                print("DO WE GET TO SORTE#D", sorted_dict)
                list_of_five_most_common_characters = sorted_dict[0:5]

                for dict_pair in list_of_five_most_common_characters:
                    five_most_common_characters.append(dict_pair[0])

                sector_id_and_checksum = chunk.split("[")
                print()

                sector_id = int(sector_id_and_checksum[0])
                print(sector_id)

                checksum = (sector_id_and_checksum[1].strip("]"))
                print(checksum)

            else:
                print("UPDATING")
                for letter in chunk:
                    dict_of_letter_and_repetition_pairs.setdefault(letter, 0)
                    dict_of_letter_and_repetition_pairs[letter] += 1

        checksum_correct_count = 0

        print("five_most_common_characters", five_most_common_characters)

        for character in checksum:

            if character in five_most_common_characters:
                checksum_correct_count += 1

            if checksum_correct_count == 5:
                is_real_room = True

        if is_real_room == True:
            sum_of_sector_ids_from_real_rooms += sector_id

    print(sum_of_sector_ids_from_real_rooms)
    return sum_of_sector_ids_from_real_rooms

if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
