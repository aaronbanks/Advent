from ..functions import run_solution

input_filename = "./inputs/201704.txt"
expected_output = 265


def solution(input_lines):

    valid_passphrases = 0

    for current_line in input_lines:
        words_on_line = current_line.split()

        anagram_exsists = False

        for word in words_on_line:

            length_of_current_word = len(word)

            characters_in_word = sorted(list(word))

            number_of_anagram_matches = 0

            for words in words_on_line:
                if len(words) != length_of_current_word:
                    pass

                if sorted(list(words)) == characters_in_word:
                    number_of_anagram_matches += 1

                if number_of_anagram_matches > 1:
                    anagram_exsists = True
                    break

        if anagram_exsists == False:
            valid_passphrases += 1

    print(f"{valid_passphrases}")

    return valid_passphrases


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
