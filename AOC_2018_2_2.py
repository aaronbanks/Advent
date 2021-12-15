from AOC_Functions import read_lines

def main():

    input = read_lines("input201802.txt")

    shared_characters = ""
    for line in input:

        box_pair_found = False

        current_line_content = []

        for character in line:
            current_line_content.append(character)

        for lines in input:

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

main()









main()
