from ..functions import run_solution

input_filename = "./inputs/202104.txt"
expected_output = None


def solution(input_lines):

    return equate_solution(find_winning_card_and_trigger_number(process_input(input_lines)))
    
def find_winning_card_and_trigger_number(bingo_numbers_and_cards):

    bingo_numbers = bingo_numbers_and_cards[0]
    dict_of_bingo_cards = bingo_numbers_and_cards[1]
    
    bingo_numbers_read = 0
    bingo = False

    for number in bingo_numbers:
        bingo_numbers_read += 1

        # CHECK EACH NUMBER ON BINGO CARD AND SEE IF IT MARCHES WITH CURRENT BINGO NUMBER:
        # IF YES, CHANGE IT'S VALUE TO "X"
        for key in dict_of_bingo_cards:
            for row in key:
                for column in row:
            
                    if number == key[row][column]:
                        key[row][column] = "X"
        
        if bingo_numbers_read > 4:

#CHECK EACH COLUMN AND ROW IN EACH BINGO CARD TO SEE IF IT'S BINGO. 
#IF YES SET BINGO_TRIGGER_NUMBER AND WINNING_BINGO_CARD

            for key in dict_of_bingo_cards:
                winning_bingo_card = []
                bingo_trigger_number = 0

                dict_of_column_values = {}

                dict_of_column_values["column_1"] = []
                dict_of_column_values["column_2"] = []
                dict_of_column_values["column_3"] = []
                dict_of_column_values["column_4"] = []
                dict_of_column_values["column_5"] = []

                while bingo == False:
                    for row in key: 
                        column_counter = 0

                        for number in row:
                            column_counter += 1
                            dict_of_column_values[f"column_{column_counter}"].append(number)

                        if bingo_check(row) == True:
                            bingo_trigger_number = bingo_numbers[bingo_numbers_read - 1]
                            winning_bingo_card = key
                            bingo = True

                    for key in dict_of_column_values:
                        if bingo_check(key) == True:
                            bingo_trigger_number = bingo_numbers[bingo_numbers_read - 1]
                            winning_bingo_card = key
                            bingo = True
                    
                    break

                return (bingo_trigger_number, winning_bingo_card)
                


def process_input(input_lines):

    dict_of_bingo_cards = {}
    current_line = 0
    current_bingo_sheet = 0

    for line in input_lines:
        current_line += 1

        if current_line == 1:
            bingo_numbers = line.split(",")
            continue
        
        if line == "":
            current_bingo_sheet += 1
            dict_of_bingo_cards[f"card{current_bingo_sheet}"]= []
            continue
        
        list_of_line_values = line.split()
        dict_of_bingo_cards[f"card{current_bingo_sheet}"].append(list_of_line_values)
    
    return (bingo_numbers, dict_of_bingo_cards)

#SUM ALL OF THE UNMARKED NUMBERS ON WINNING BOARD, THEN MULTIPLY THAT SUM BY THE BINGO_TRIGGER_NUMBER
def equate_solution(winning_board, bingo_trigger_number):
    sum_of_unmarked_numbers = 0

    for row in winning_board:
        for number in row:
            if number == "X":
                pass
            else:
                sum_of_unmarked_numbers += int(number)

    return sum_of_unmarked_numbers * bingo_trigger_number

def bingo_check(line):
    for number in line:
        if number == "X":
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
