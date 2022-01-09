from ..functions import run_solution

input_filename = "./inputs/202104.txt"
expected_output = None


def solution(input_lines):

    current_line = 0

    bingo_numbers = []

    current_bingo_sheet = 0

    dict_of_bingo_cards = {}

    for line in input_lines:
        current_line += 1

        if current_line == 1:
            bingo_numbers = line.split(",")
        
        if line == "":
            current_bingo_sheet += 1
            dict_of_bingo_cards[f"card{current_bingo_sheet}"]= []
            pass
        
        list_of_line_values = line.split()
        dict_of_bingo_cards[f"card{current_bingo_sheet}"].append(list_of_line_values)

    bingo_numbers_read = 0

    for number in bingo_numbers:
        bingo_numbers_read += 1

        for key in dict_of_bingo_cards:
            for row in key:
                for column in row:
            
                    if number == key[row][column]:
                        key[row][column] = "X"
        
        bingo = False

        if bingo_numbers_read > 4:

#CHECK IF EACH ROW IS A BINGO
            for key in dict_of_bingo_cards:
                for row in key: 
#CHECK IF EACH COLUMN IS A BINGO

#IF BINGO = TRUE, IDENTIDY WHICH BOARD ACHIEVED BINGO AND WHICH NUMBER WAS THE BINGO_TRIGGER_NUMBWER

#SUM ALL OF THE UNMARKED NUMBERS ON WINNING BOARD, THEN MULTIPLY THAT SUM BY THE BINGO_TRIGGER_NUMBER



if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
