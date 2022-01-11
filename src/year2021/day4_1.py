from ..functions import run_solution

input_filename = "./inputs/202104.txt"
expected_output = None


def solution(input_lines):

    return equate_solution(*find_winning_card_and_trigger_number(*process_input(input_lines)))
    

def process_input(input_lines):

    dict_of_bingo_cards = {}
    bingo_numbers = []

    first_line = True
    current_bingo_sheet = 0

    for line in input_lines:
        if first_line == True:
            bingo_numbers = line.split(",")
            first_line = False
            continue

        if line == "":
            current_bingo_sheet += 1
            dict_of_bingo_cards[f"card{current_bingo_sheet}"]= []
            continue
        
        list_of_line_values = line.split()
        dict_of_bingo_cards[f"card{current_bingo_sheet}"].append(list_of_line_values)
    
    return (bingo_numbers, dict_of_bingo_cards)

def bingo_check(line):
    for number in line:
        if number == "X":
            pass
        else:
            return False
    return True

def find_winning_card_and_trigger_number(bingo_numbers, dict_of_bingo_cards):

    bingo_numbers_read = 0
    bingo = False

    winning_bingo_card = []
    bingo_trigger_number = 0

    for number in bingo_numbers:
        bingo_numbers_read += 1

        for key in dict_of_bingo_cards:
            for row in key:
                for column in row:
            
                    if number == column:
                        key[row][column] = "X"
        
        if bingo_numbers_read > 4:

            for key in dict_of_bingo_cards:

                dict_of_column_values = {}

                dict_of_column_values["column_1"] = []
                dict_of_column_values["column_2"] = []
                dict_of_column_values["column_3"] = []
                dict_of_column_values["column_4"] = []
                dict_of_column_values["column_5"] = []

                
                for row in key: 
                    column_counter = 0

                    for number in row:
                        column_counter += 1
                        dict_of_column_values[f"column_{column_counter}"].append(number)

                    if bingo_check(row) == True:
                        bingo_trigger_number = bingo_numbers[bingo_numbers_read - 1]
                        winning_bingo_card = key
                        bingo = True

                if bingo == True:
                    break

                for key in dict_of_column_values:
                    if bingo_check(key) == True:
                        bingo_trigger_number = bingo_numbers[bingo_numbers_read - 1]
                        winning_bingo_card = key
                        bingo = True
                        break

                if bingo == False:
                    return "ERROR NO BINGO"

                return (bingo_trigger_number, winning_bingo_card)
                
def equate_solution(bingo_trigger_number, winning_bingo_card):
    sum_of_unmarked_numbers = 0

    for row in winning_bingo_card:
        for number in row:
            if number == "X":
                pass
            else:
                sum_of_unmarked_numbers += int(number)

    return sum_of_unmarked_numbers * bingo_trigger_number


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
