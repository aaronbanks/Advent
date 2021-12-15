from ..functions import read_lines

def main():

    input = read_lines("./inputs/202002.txt")

    valid_passwords = 0

    for line in input:
        current_line_contents = line.split(": ", 2 )

        password_policy = current_line_contents[0]
        password = current_line_contents[1]

        policy = password_policy.split()

        policy_letter = policy[1]

        policy_numbers = policy[0].split("-")

        policy_upper_limit = int(policy_numbers[1])
        policy_lower_limit = int(policy_numbers[0])

        policy_range = range(policy_lower_limit, policy_upper_limit + 1)

        character_count  = 0

        for character in password:
            if character == policy_letter:
                character_count += 1

        if character_count in policy_range:
            valid_passwords += 1

    print(valid_passwords)

main()
