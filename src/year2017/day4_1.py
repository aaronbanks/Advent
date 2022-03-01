from ..functions import run_solution

input_filename = "./inputs/201704.txt"
expected_output = 383

def solution(input_lines):

    valid_passphrases = 0

    for current_line in input_lines:
        words_on_line = current_line.split()

        duplicate_word = False

        for word in words_on_line:

            number_of_matches = 0

            for words in words_on_line:
                if word == words:
                    number_of_matches += 1

            if number_of_matches > 1:
                duplicate_word = True
                break
        
        if duplicate_word == False:
            valid_passphrases += 1

    print (f"{valid_passphrases}")

    return valid_passphrases

if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
