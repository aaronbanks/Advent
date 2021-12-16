from ..functions import run_solution
import math

input_filename = "./inputs/201901.txt"
expected_output = 3263320


def solution(input_lines):

    total_fuel_req = 0

    for module in input_lines:
        mass = float(module)

        fuel_req = int(math.floor(mass / 3) - 2)

        total_fuel_req += fuel_req

    print(total_fuel_req)
    return total_fuel_req


if __name__ == "__main__":
    run_solution(solution, input_filename, expected_solution)
