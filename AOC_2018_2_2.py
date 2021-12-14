from AOC_Functions import read_lines

def main():

    # checksum = 0
    # boxes_with_two_of_same = 0
    # boxes_with_three_of_same = 0

    input = read_lines("input201802.txt")

    for line in input:
    #
    #     set_of_characters_counted = set()
    #
    #     box_has_two_of_same = False
    #     box_has_three_of_same = False
    #
    #     for character in line:
    #         if character in set_of_characters_counted:
    #             continue
    #
    #         set_of_characters_counted.add(character)
    #
    #         counter = line.count(character)
    #
    #         if counter == 2 and box_has_two_of_same == False:
    #             boxes_with_two_of_same += 1
    #             box_has_two_of_same = True
    #
    #         if counter == 3 and box_has_three_of_same == False:
    #             boxes_with_three_of_same += 1
    #             box_has_three_of_same == True
    #
    # checksum = boxes_with_two_of_same * boxes_with_three_of_same
    # print(checksum)

main()
