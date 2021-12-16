from ..functions import run_solution

input_filename = "./inputs/202002.txt"
expected_output = 251


def solution(input_lines):

    valid_passwords = 0

    for line in input_lines:
        current_line_contents = line.split(": ", 2)

        password_policy = current_line_contents[0]
        password = current_line_contents[1]

        policy = password_policy.split()

        policy_letter = policy[1]

        policy_numbers = policy[0].split("-")

        letter_position_one = int(policy_numbers[0]) - 1
        letter_position_two = int(policy_numbers[1]) - 1

        positions_containing_letter = 0

        if password[letter_position_one] == policy_letter:
            positions_containing_letter += 1

        if password[letter_position_two] == policy_letter:
            positions_containing_letter += 1

        if positions_containing_letter == 1:
            valid_passwords += 1

    print(valid_passwords)
    return valid_passwords


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
