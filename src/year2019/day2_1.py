from ..functions import run_solution

input_filename = "./inputs/201902.txt"
expected_output = 3101878


def solution(input_lines):

    intcode = list(map(int, input_lines[0].split(",")))

    intcode[1] = 12
    intcode[2] = 2

    print(f"Starting intcode: {intcode}")

    location_counter = 0
    loop_counter = 0

    while True:

        loop_counter += 1

        opcode = intcode[location_counter]

        if opcode == 1:
            intcode[intcode[location_counter + 3]] = (
                intcode[intcode[location_counter + 1]]
                + intcode[intcode[location_counter + 2]]
            )

        elif opcode == 2:
            intcode[intcode[location_counter + 3]] = (
                intcode[intcode[location_counter + 1]]
                * intcode[intcode[location_counter + 2]]
            )

        elif opcode == 99:
            break

        else:
            print("opcode alignment error")

        print(f"On loop #{loop_counter} the updated intcode is: {intcode}")
        location_counter += 4

    print(f"Ending intcode: {intcode}")

    return intcode[0]


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
