from ..functions import run_solution

input_filename = "./inputs/202004.txt"
expected_output = None


def solution(input_lines):

    number_of_valid_passports = 0

    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    #cid = False

    list_of_fields = [
        byr,
        iyr,
        eyr,
        hgt,
        hcl,
        ecl,
        pid,
        #cid,
    ]

    field_value_dict = {}

    for current_line in input_lines:

        all_fields_used = True

        if current_line == "":
            for field in list_of_fields:
                #The error is here, obviously the bool doesn't match any of the keys.
                if field in field_value_dict.keys():
                    field = True

            for field in list_of_fields:
                if field == True:
                    pass
                else:
                    all_fields_used = False

            if all_fields_used == True:
                number_of_valid_passports += 1

            for field in list_of_fields:
                field = False
            field_value_dict.clear()

        else:

            key_value_pairs = current_line.split()

            for pair in key_value_pairs:
                split_pair = pair.split(":")

                field_value_dict[split_pair[0]] = split_pair[1]

    print(f"The number of valid passports is: {number_of_valid_passports}")
    return number_of_valid_passports


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
