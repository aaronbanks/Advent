from ..functions import run_solution

input_filename = "./inputs/201706.txt"
expected_output = 0


def solution(input_lines):

    character_storage = input_lines[0].split("\t")

    bank_block_allocation = [int(x) for x in character_storage]

    set_of_bank_configurations = {tuple(bank_block_allocation)}

    cycles_completed = 0

    repeating_pattern = []
    cycles_in_infinate_loop = 0
    inside_infinate_loop = False

    while True:

        highest_value_block = find_highest_bank_location_and_value(
            bank_block_allocation
        )

        blocks_to_distribute = highest_value_block[1]
        bank_block_allocation[highest_value_block[0]] = 0

        current_location = (highest_value_block[0] + 1) % 16

        while blocks_to_distribute > 0:

            bank_block_allocation[current_location] += 1
            blocks_to_distribute -= 1

            current_location = (current_location + 1) % 16

        cycles_completed += 1

        if inside_infinate_loop == True:
            cycles_in_infinate_loop += 1
            print(bank_block_allocation)

            # THE ISSUE IS ON THE BELOW LLINE, NEED TO FIGURE OUT HOW TO COMPAIR THESE TWO LISTS
            if bank_block_allocation == repeating_pattern:
                print(
                    f"Each iteration of the infinite loop contains: {cycles_in_infinate_loop} cycles"
                )
                return cycles_in_infinate_loop

        if tuple(bank_block_allocation) in set_of_bank_configurations:
            print(f"Infinite loop is detected at the end of cycle #{cycles_completed}")
            repeating_pattern = bank_block_allocation
            inside_infinate_loop = True
            print(bank_block_allocation)

        else:
            set_of_bank_configurations.add(tuple(bank_block_allocation))


def find_highest_bank_location_and_value(bank_block_allocation):

    highest_block_value = 0
    location_of_highest_block_count = 0
    current_bank_counter = 0

    for bank in bank_block_allocation:
        if bank > highest_block_value:
            highest_block_value = bank
            location_of_highest_block_count = current_bank_counter
        else:
            pass

        current_bank_counter += 1

    highest_location_and_value = (location_of_highest_block_count, highest_block_value)

    return highest_location_and_value


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_output)
